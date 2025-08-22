// Canvas-Style Code Synthesis Webapp
// ------------------------------------------------------------
// What this is:
// A single-file React component that renders a canvas-like UI to:
//  1) Take a natural-language Problem Description
//  2) Generate/Display Requirements (functional + non-functional)
//  3) Generate/Display Test Cases
//  4) Show Candidate Codes with metadata (complexity, robustness, etc.)
//  5) Auto-score and pick the most suitable code on the right panel
//
// Notes:
// - Pure front-end. You can later swap the mock "generate" with your LLM/backend.
// - TailwindCSS-based, no external UI lib required. (Works fine in ChatGPT canvas.)
// - Uses framer-motion + lucide-react optionally (available in this environment).
// - Drop-in ready for Next.js or Vite (TSX). Default export is a React component.
//
// Customization hints:
// - Replace `seedFromPrimeProblem()` with your own generator that calls your API.
// - Extend `scoreCandidate()` to weigh fit differently.
// - Add more Steps/Cards if your PDF flow has additional items.

import React, { useMemo, useState } from "react";
import { motion } from "framer-motion";
import {
    Brain,
    FileText,
    Beaker,
    Code as CodeIcon,
    CheckCircle2,
    XCircle,
    Sparkles,
    Copy as CopyIcon,
    ListChecks,
} from "lucide-react";

// --------------------------- Types ---------------------------

type Requirement = {
    id: string;
    kind: "functional" | "nonfunctional";
    title: string;
    details?: string[];
    category?: "performance" | "robustness" | "maintainability" | "other";
    mandatory?: boolean; // required to be satisfied
};

type TestCase = {
    id: string;
    title: string;
    code: string; // human-readable pseudo/asserts
    fromReqIds?: string[]; // which generated requirements this test derives from
};

type Candidate = {
    id: string;
    name: string;
    language: string;
    origin?: "archcode" | "existing" | "other";
    variant?: string;
    code: string;
    metrics: {
        timeComplexityRank: number; // lower is better, e.g., O(1)=1, O(log n)=2, O(\u221a n)=3, O(n)=4, O(n log n)=5, O(n^2)=6
        timeComplexityLabel: string;
        cyclomaticComplexity: number;
        robustInputChecks: boolean;
        handlesNegativesAndZero: boolean;
        notes?: string[];
    };
    rationale?: string[]; // why it exists / how it was produced
};

type GenerationBundle = {
    problem: string;
    requirements: Requirement[];
    tests: TestCase[];
    candidates: Candidate[];
};

// ---------------------- Seeded Example -----------------------
// This mirrors the flow shown in your PDF (Problem -> Requirements ->
// Test Cases -> Code + Metrics) using the classic x_or_y / primality task.

function seedFromPrimeProblem(problem: string): GenerationBundle {
    // Requirements derived from the PDF flow
    const requirements: Requirement[] = [
        {
            id: "fr-io",
            kind: "functional",
            title: "Function takes integer n and values x, y; returns a single value.",
            details: ["Signature: x_or_y(n, x, y)"],
            mandatory: true,
        },
        {
            id: "fr-behavior",
            kind: "functional",
            title: "Return x if n is prime; otherwise return y.",
            mandatory: true,
        },
        {
            id: "fr-edges",
            kind: "functional",
            title: "Edge cases",
            details: [
                "If n < 0 => return y",
                "If n == 0 => return y",
            ],
            mandatory: true,
        },
        {
            id: "nfr-perf",
            kind: "nonfunctional",
            category: "performance",
            title: "Time complexity O(\u221a n) for primality check; responsive under 5s for huge n.",
            mandatory: true,
        },
        {
            id: "nfr-robust",
            kind: "nonfunctional",
            category: "robustness",
            title: "Robustness",
            details: [
                "If n is not an integer => print error to stderr and return None",
                "If x or y not numeric => print error to stderr and return None",
            ],
        },
        {
            id: "nfr-maint",
            kind: "nonfunctional",
            category: "maintainability",
            title: "Cyclomatic Complexity \u2264 5",
        },
    ];

    // From the PDF test style (assert-like)
    const tests: TestCase[] = [
        {
            id: "t1",
            title: "Prime returns x",
            code: "assert x_or_y(13, 77, 2) == 77",
            fromReqIds: ["fr-behavior", "fr-io"],
        },
        {
            id: "t2",
            title: "Composite returns y",
            code: "assert x_or_y(24, 8, 9) == 9",
            fromReqIds: ["fr-behavior", "fr-io"],
        },
        {
            id: "t3",
            title: "Negative n returns y",
            code: "assert x_or_y(-7, 77, -5) == -5",
            fromReqIds: ["fr-edges", "fr-io"],
        },
        { id: "t4", title: "Zero returns y", code: "assert x_or_y(0, 77, 0) == 0", fromReqIds: ["fr-edges", "fr-io"] },
        {
            id: "t5",
            title: "Large prime",
            code: "assert x_or_y(2**31-1, 34, 0) == 34",
            fromReqIds: ["fr-behavior", "nfr-perf", "fr-io"],
        },
        {
            id: "t6",
            title: "Non-int n handled",
            code: "assert not x_or_y('invalid', 34, 0)",
            fromReqIds: ["nfr-robust"],
        },
        {
            id: "t7",
            title: "Complexity bound",
            code: "assert ComplexityVisitor.total_complexity('x_or_y') <= 5",
            fromReqIds: ["nfr-maint"],
        },
    ];

    // Two representative candidates ("Existing" vs. "ARCHCODE-like")
    const candidates: Candidate[] = [
        {
            id: "cand-existing",
            name: "Existing Methods (naive)",
            origin: "existing",
            language: "python",
            code: `def x_or_y(n, x, y):
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
    return x`,
            metrics: {
                timeComplexityRank: 4,
                timeComplexityLabel: "O(n)",
                cyclomaticComplexity: 4,
                robustInputChecks: false,
                handlesNegativesAndZero: false,
                notes: ["Simple but slower primality check", "No input validation"],
            },
            rationale: ["Straightforward for small n", "Often seen as a baseline implementation"],
        },
        {
            id: "cand-arch-v1",
            name: "ARCHCODE v1 — √n trial division + checks",
            origin: "archcode",
            language: "python",
            code: `import sys, math

def _is_prime(n):
    if not isinstance(n, int):
        sys.stderr.write("Invalid input: n must be an integer.
")
        return None
    if n < 2:
        return False
    r = int(math.isqrt(n))
    for i in range(2, r + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        sys.stderr.write("Invalid input: x and y must be numeric values.
")
        return None
    prime = _is_prime(n)
    if prime is None:
        return None
    return x if prime else y
`,
            metrics: {
                timeComplexityRank: 3,
                timeComplexityLabel: "O(√n)",
                cyclomaticComplexity: 5,
                robustInputChecks: true,
                handlesNegativesAndZero: true,
                notes: ["Validates types", "Uses isqrt", "Early reject <2"],
            },
            rationale: ["Baseline ARCHCODE with clear structure"],
        },
        {
            id: "cand-arch-v2",
            name: "ARCHCODE v2 — 6k±1 wheel (faster constants)",
            origin: "archcode",
            language: "python",
            code: `import sys, math

def _is_prime(n):
    if not isinstance(n, int):
        sys.stderr.write("Invalid input: n must be an integer.
")
        return None
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    r = int(math.isqrt(n))
    i = 5
    while i <= r:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def x_or_y(n, x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        sys.stderr.write("Invalid input: x and y must be numeric values.
")
        return None
    prime = _is_prime(n)
    if prime is None:
        return None
    return x if prime else y
`,
            metrics: {
                timeComplexityRank: 3,
                timeComplexityLabel: "O(√n) (6k±1)",
                cyclomaticComplexity: 5,
                robustInputChecks: true,
                handlesNegativesAndZero: true,
                notes: ["Skips multiples of 2 and 3", "Lower constant factor"],
            },
            rationale: ["Optimized trial division via 6k±1"],
        },
        {
            id: "cand-arch-v3",
            name: "ARCHCODE v3 — Miller–Rabin (prob.)",
            origin: "archcode",
            language: "python",
            code: `import sys

def _is_prime(n):
    if not isinstance(n, int):
        sys.stderr.write("Invalid input: n must be an integer.
")
        return None
    if n < 2:
        return False
    small = [2,3,5,7,11,13,17,19,23,29]
    if n in small:
        return True
    if any(n % p == 0 for p in small):
        return False
    # write n-1 as d*2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # bases 2,7,61 are deterministic for 32-bit ints
    for a in [2, 7, 61]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def x_or_y(n, x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        sys.stderr.write("Invalid input: x and y must be numeric values.
")
        return None
    prime = _is_prime(n)
    if prime is None:
        return None
    return x if prime else y
`,
            metrics: {
                timeComplexityRank: 2,
                timeComplexityLabel: "O(k·log^3 n) (prob.)",
                cyclomaticComplexity: 7,
                robustInputChecks: true,
                handlesNegativesAndZero: true,
                notes: ["Probabilistic test with fixed bases", "Very fast for large n"],
            },
            rationale: ["Fast probabilistic check for very large n"],
        },
    ];

    return { problem, requirements, tests, candidates };
}

// ---------------------- Scoring / Selection ----------------------

const COMPLEXITY_TARGET_RANK = 3; // O(\u221a n)

function scoreCandidate(c: Candidate, reqs: Requirement[]): { score: number; reasons: string[]; ok: boolean } {
    let score = 0;
    const reasons: string[] = [];

    // Mandatory functional reqs must be met (we infer from metadata heuristics)
    let functionalOK = true;

    // Edge handling heuristic
    const needsEdgeHandling = reqs.some((r) => r.id === "fr-edges");
    if (needsEdgeHandling) {
        if (c.metrics.handlesNegativesAndZero) {
            score += 25;
            reasons.push("Meets edge cases for negatives and zero");
        } else {
            functionalOK = false;
            reasons.push("Fails required edge cases (negatives/zero)");
        }
    }

    // Complexity target
    if (c.metrics.timeComplexityRank <= COMPLEXITY_TARGET_RANK) {
        score += 20;
        reasons.push(`Meets complexity target (${c.metrics.timeComplexityLabel})`);
    } else {
        reasons.push(`Slower than target (${c.metrics.timeComplexityLabel})`);
    }

    // Robustness
    const wantsRobustness = reqs.some((r) => r.id === "nfr-robust");
    if (wantsRobustness && c.metrics.robustInputChecks) {
        score += 15;
        reasons.push("Has input validations (robustness)");
    }

    // Maintainability
    const wantsMaintainability = reqs.some((r) => r.id === "nfr-maint");
    if (wantsMaintainability && c.metrics.cyclomaticComplexity <= 5) {
        score += 10;
        reasons.push("Cyclomatic complexity \u2264 5");
    }

    // Baseline + rationale bonus
    score += Math.max(0, 10 - c.metrics.cyclomaticComplexity);
    if (c.rationale?.length) score += 5;

    const ok = functionalOK; // we could extend with more checks
    return { score, reasons, ok };
}

// --------------------------- UI Bits ---------------------------

// Color tokens for Requirements + Test mapping
const REQ_COLOR_PALETTE = [
    { bg: "bg-emerald-50", text: "text-emerald-700", border: "border-emerald-300", dot: "bg-emerald-500", ring: "ring-emerald-200" },
    { bg: "bg-sky-50",     text: "text-sky-700",     border: "border-sky-300",     dot: "bg-sky-500",     ring: "ring-sky-200" },
    { bg: "bg-amber-50",   text: "text-amber-800",   border: "border-amber-300",   dot: "bg-amber-500",   ring: "ring-amber-200" },
    { bg: "bg-violet-50",  text: "text-violet-700",  border: "border-violet-300",  dot: "bg-violet-500",  ring: "ring-violet-200" },
    { bg: "bg-rose-50",    text: "text-rose-700",    border: "border-rose-300",    dot: "bg-rose-500",    ring: "ring-rose-200" },
    { bg: "bg-teal-50",    text: "text-teal-700",    border: "border-teal-300",    dot: "bg-teal-500",    ring: "ring-teal-200" },
    { bg: "bg-lime-50",    text: "text-lime-700",    border: "border-lime-300",    dot: "bg-lime-500",    ring: "ring-lime-200" },
    { bg: "bg-fuchsia-50", text: "text-fuchsia-700", border: "border-fuchsia-300", dot: "bg-fuchsia-500", ring: "ring-fuchsia-200" },
] as const;

function Badge({ children, className = "" }: { children: React.ReactNode; className?: string }) {
    return (
        <span className={`inline-flex items-center rounded-full border px-2 py-0.5 text-xs font-medium text-gray-600 ${className}`}>
      {children}
    </span>
    );
}

function CardBox({
                     icon,
                     title,
                     right,
                     children,
                 }: {
    icon?: React.ReactNode;
    title: string;
    right?: React.ReactNode;
    children: React.ReactNode;
}) {
    return (
        <div className="rounded-2xl border bg-white/70 backdrop-blur shadow-sm p-4 md:p-5">
            <div className="flex items-center justify-between mb-3">
                <div className="flex items-center gap-2 text-gray-800">
                    {icon}
                    <h3 className="font-semibold tracking-tight">{title}</h3>
                </div>
                {right}
            </div>
            {children}
        </div>
    );
}

function MonoBlock({ code, className }: { code: string; className?: string }) {
    return (
        <pre className={`rounded-xl border bg-neutral-50 p-3 overflow-auto text-sm leading-relaxed ${className ?? ""}`}>
      <code>{code}</code>
    </pre>
    );
}

function CopyButton({ text }: { text: string }) {
    const [copied, setCopied] = useState(false);
    return (
        <button
            onClick={() => {
                navigator.clipboard.writeText(text).then(() => {
                    setCopied(true);
                    setTimeout(() => setCopied(false), 1200);
                });
            }}
            className="inline-flex items-center gap-1 rounded-xl border px-2.5 py-1 text-sm hover:bg-gray-50"
            title="Copy to clipboard"
        >
            <CopyIcon className="h-4 w-4" /> {copied ? "Copied!" : "Copy"}
        </button>
    );
}

// --------------------------- Main ---------------------------

export default function CanvasStyleCodeSynthesis() {
    const [problem, setProblem] = useState<string>(
        "A simple program which should return the value of x if n is a prime number and should return the value of y otherwise."
    );
    const [bundle, setBundle] = useState<GenerationBundle | null>(() => seedFromPrimeProblem(
        "A simple program which should return the value of x if n is a prime number and should return the value of y otherwise."
    ));

    const [selectedId, setSelectedId] = useState<string | null>(null);

    const scored = useMemo(() => {
        if (!bundle) return [] as { c: Candidate; score: number; ok: boolean; reasons: string[] }[];
        return bundle.candidates.map((c) => {
            const { score, ok, reasons } = scoreCandidate(c, bundle.requirements);
            return { c, score, ok, reasons };
        });
    }, [bundle]);

    const best = useMemo(() => {
        if (!scored.length) return null;
        const okOnly = scored.filter((s) => s.ok);
        const winner = (okOnly.length ? okOnly : scored).slice().sort((a, b) => b.score - a.score)[0];
        return winner;
    }, [scored]);

    const selected = useMemo(() => {
        if (!bundle) return null;
        const id = selectedId ?? best?.c.id ?? null;
        return id ? bundle.candidates.find((c) => c.id === id) ?? null : null;
    }, [bundle, best, selectedId]);

    const reqIndexMap = useMemo(() => new Map((bundle?.requirements ?? []).map((r, i) => [r.id, i])), [bundle]);

    const colorFor = (rid: string) => {
        const idx = reqIndexMap.get(rid) ?? 0;
        return REQ_COLOR_PALETTE[idx % REQ_COLOR_PALETTE.length];
    };

    const reqLabel = (rid: string) => {
        const r = bundle?.requirements.find((x) => x.id === rid);
        if (!r) return rid;
        const prefix = r.kind === "functional" ? "FR" : "NFR";
        return `${prefix}: ${r.title}`;
    };

    function handleGenerate() {
        // If the problem text appears to be the primality task, use the seeded flow.
        const p = problem.trim();
        const looksPrime = /prime|\b소수\b|\bn is a prime/i.test(p);

        if (looksPrime) {
            const seeded = seedFromPrimeProblem(p);
            setBundle(seeded);
            // Auto-select best
            const w = seeded.candidates
                .map((c) => ({ c, ...scoreCandidate(c, seeded.requirements) }))
                .sort((a, b) => b.score - a.score)[0];
            setSelectedId(w.c.id);
            return;
        }

        // Otherwise create a minimal skeleton; you can wire your own backend here
        const basic: GenerationBundle = {
            problem: p,
            requirements: [
                {
                    id: "fr-1",
                    kind: "functional",
                    title: "Define function meeting the described behavior.",
                    mandatory: true,
                },
                {
                    id: "nfr-perf",
                    kind: "nonfunctional",
                    category: "performance",
                    title: "Reasonable time complexity for input size.",
                },
            ],
            tests: [
                { id: "t1", title: "Happy path", code: "# TODO: add asserts", fromReqIds: ["fr-1"] },
                { id: "t2", title: "Edge cases", code: "# TODO: add asserts", fromReqIds: ["fr-1"] },
            ],
            candidates: [
                {
                    id: "cand-a",
                    name: "Candidate A",
                    language: "python",
                    code: "# TODO: generated code here\n",
                    metrics: {
                        timeComplexityRank: 4,
                        timeComplexityLabel: "O(n)",
                        cyclomaticComplexity: 4,
                        robustInputChecks: false,
                        handlesNegativesAndZero: false,
                    },
                },
            ],
        };
        setBundle(basic);
        setSelectedId("cand-a");
    }

    return (
        <div className="min-h-screen w-full bg-gradient-to-br from-slate-50 to-slate-100 text-gray-900">
            {/* Header */}
            <div className="sticky top-0 z-10 border-b bg-white/70 backdrop-blur">
                <div className="mx-auto max-w-7xl px-4 py-3 flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <Sparkles className="h-5 w-5" />
                        <span className="font-semibold">Canvas Code Builder</span>
                    </div>
                    <div className="flex items-center gap-2 text-sm">
                        <Badge>Front-end only</Badge>
                        <Badge>LLM-ready hooks</Badge>
                    </div>
                </div>
            </div>

            <main className="mx-auto max-w-7xl px-4 py-6 grid grid-cols-12 gap-5">
                {/* Flow column */}
                <div className="col-span-12 space-y-5">
                    <CardBox
                        icon={<FileText className="h-5 w-5" />}
                        title="1) Problem Description"
                        right={
                            <button
                                onClick={handleGenerate}
                                className="inline-flex items-center gap-2 rounded-2xl border px-3 py-1.5 text-sm hover:bg-gray-50"
                                title="Generate requirements, tests and candidates"
                            >
                                <Brain className="h-4 w-4" /> Generate
                            </button>
                        }
                    >
            <textarea
                className="w-full min-h-[120px] rounded-xl border p-3 focus:outline-none focus:ring-2 focus:ring-indigo-300"
                value={problem}
                onChange={(e) => setProblem(e.target.value)}
                placeholder="Describe what the program must do..."
            />
                        <div className="mt-2 text-xs text-gray-500">
                            Tip: Paste any task. If it mentions primes/소수, a rich example will load.
                        </div>
                    </CardBox>

                    <CardBox icon={<ListChecks className="h-5 w-5" />} title="2) Generated Requirements">
                        {!bundle ? (
                            <div className="text-sm text-gray-500">No requirements yet. Click Generate.</div>
                        ) : (
                            <div className="space-y-3">
                                <div>
                                    <div className="mb-1 text-xs uppercase tracking-wide text-gray-500">Functional</div>
                                    <ul className="space-y-1">
                                        {bundle.requirements
                                            .filter((r) => r.kind === "functional")
                                            .map((r) => (
                                                <li key={r.id} className={`flex items-start gap-2 rounded-lg border p-3 ${colorFor(r.id).bg} ${colorFor(r.id).border}`}>
                                                    <CheckCircle2 className={`mt-0.5 h-4 w-4 ${colorFor(r.id).text}`} />
                                                    <div>
                                                        <div className="text-sm font-medium">{r.title}</div>
                                                        {!!r.details?.length && (
                                                            <ul className="mt-1 list-disc pl-5 text-xs text-gray-600">
                                                                {r.details.map((d, i) => (
                                                                    <li key={i}>{d}</li>
                                                                ))}
                                                            </ul>
                                                        )}
                                                    </div>
                                                </li>
                                            ))}
                                    </ul>
                                </div>
                                <div>
                                    <div className="mb-1 text-xs uppercase tracking-wide text-gray-500">Non-Functional</div>
                                    <ul className="space-y-1">
                                        {bundle.requirements
                                            .filter((r) => r.kind === "nonfunctional")
                                            .map((r) => (
                                                <li key={r.id} className={`flex items-start gap-2 rounded-lg border p-3 ${colorFor(r.id).bg} ${colorFor(r.id).border}`}>
                                                    <Beaker className={`mt-0.5 h-4 w-4 ${colorFor(r.id).text}`} />
                                                    <div>
                                                        <div className="text-sm font-medium">{r.title}</div>
                                                        {!!r.details?.length && (
                                                            <ul className="mt-1 list-disc pl-5 text-xs text-gray-600">
                                                                {r.details.map((d, i) => (
                                                                    <li key={i}>{d}</li>
                                                                ))}
                                                            </ul>
                                                        )}
                                                    </div>
                                                </li>
                                            ))}
                                    </ul>
                                </div>
                            </div>
                        )}
                    </CardBox>

                    <CardBox icon={<Beaker className="h-5 w-5" />} title="3) Generated Test Cases">
                        {!bundle ? (
                            <div className="text-sm text-gray-500">No tests yet. Click Generate.</div>
                        ) : (
                            <div className="space-y-2">
                                {bundle.tests.map((t) => (
                                    <div key={t.id} className="rounded-xl border bg-white p-3">
                                        <div className="text-sm font-medium mb-1">{t.title}</div>
                                        {t.fromReqIds?.length ? (
                                            <div className="mb-2 flex flex-wrap gap-1">
                                                {t.fromReqIds.map((rid) => (
                                                    <Badge key={rid} className={`${colorFor(rid).bg} ${colorFor(rid).border} ${colorFor(rid).text}`}>{reqLabel(rid)}</Badge>
                                                ))}
                                            </div>
                                        ) : null}
                                        <MonoBlock code={t.code} />
                                    </div>
                                ))}
                            </div>
                        )}
                    </CardBox>

                    <CardBox icon={<CodeIcon className="h-5 w-5" />} title="4) Candidate Codes">
                        {!bundle ? (
                            <div className="text-sm text-gray-500">No candidates yet. Click Generate.</div>
                        ) : (
                            <div className="space-y-4">
                                {scored.map(({ c, score, ok, reasons }) => (
                                    <motion.div
                                        key={c.id}
                                        initial={{ opacity: 0, y: 6 }}
                                        animate={{ opacity: 1, y: 0 }}
                                        transition={{ duration: 0.25 }}
                                        className={`w-full h-full flex flex-col rounded-2xl border p-3 ${
                                            selectedId === c.id ? "ring-2 ring-indigo-400" : ""
                                        }`}
                                    >
                                        <div className="flex items-start justify-between gap-2">
                                            <div>
                                                <div className="font-medium">{c.name}</div>
                                                <div className="text-xs text-gray-500 flex items-center gap-1">{c.language.toUpperCase()}{c.origin === "archcode" ? (<Badge className="bg-indigo-50 border-indigo-300 text-indigo-700">ARCHCODE</Badge>) : null}</div>
                                            </div>
                                            <div className="text-right text-xs">
                                                <div>
                                                    Score: <span className="font-semibold">{score}</span>
                                                </div>
                                                <div className={ok ? "text-emerald-600" : "text-amber-600"}>
                                                    {ok ? "Meets" : "May violate"} required FRs
                                                </div>
                                            </div>
                                        </div>
                                        <div className="mt-2 flex flex-wrap gap-1.5 text-xs">
                                            <Badge>Complexity: {c.metrics.timeComplexityLabel}</Badge>
                                            <Badge>CC: {c.metrics.cyclomaticComplexity}</Badge>
                                            <Badge>{c.metrics.robustInputChecks ? "Robust" : "No checks"}</Badge>
                                            <Badge>{c.metrics.handlesNegativesAndZero ? "Edge-safe" : "Edge-unsafe"}</Badge>
                                        </div>
                                        {c.metrics.notes?.length ? (
                                            <ul className="mt-2 list-disc pl-5 text-xs text-gray-600">
                                                {c.metrics.notes.map((n, i) => (
                                                    <li key={i}>{n}</li>
                                                ))}
                                            </ul>
                                        ) : null}
                                        <div className="mt-3">
                                            <MonoBlock code={c.code} className="max-h-48" />
                                        </div>
                                        <div className="mt-2 flex items-center justify-between">
                                            <button
                                                onClick={() => setSelectedId(c.id)}
                                                className="inline-flex items-center gap-2 rounded-xl border px-3 py-1.5 text-sm hover:bg-gray-50"
                                                title="Select this code for the right panel"
                                            >
                                                {selectedId === c.id ? (
                                                    <>
                                                        <CheckCircle2 className="h-4 w-4 text-emerald-600" /> Selected
                                                    </>
                                                ) : (
                                                    <>
                                                        <CodeIcon className="h-4 w-4" /> Use this
                                                    </>
                                                )}
                                            </button>
                                            <CopyButton text={c.code} />
                                        </div>
                                        {reasons.length ? (
                                            <div className="mt-2 text-xs text-gray-600">
                                                <div className="mb-1 font-medium">Why this score:</div>
                                                <ul className="list-disc pl-5">
                                                    {reasons.map((r, i) => (
                                                        <li key={i}>{r}</li>
                                                    ))}
                                                </ul>
                                            </div>
                                        ) : null}
                                    </motion.div>
                                ))}
                            </div>
                        )}
                    </CardBox>
                </div>

                {/* Selection column */}
                <div className="col-span-12 space-y-5">
                    <CardBox icon={<CheckCircle2 className="h-5 w-5" />} title="5) Selected Code">
                        {!selected ? (
                            <div className="text-sm text-gray-500">No selection. Generate and pick a candidate.</div>
                        ) : (
                            <>
                                <div className="flex items-center justify-between">
                                    <div>
                                        <div className="text-sm text-gray-500">Chosen Candidate</div>
                                        <div className="text-lg font-semibold">{selected.name}</div>
                                    </div>
                                    <CopyButton text={selected.code} />
                                </div>
                                <div className="mt-3">
                                    <MonoBlock code={selected.code} className="min-h-[240px]" />
                                </div>
                                <div className="mt-3 grid grid-cols-2 gap-2 text-sm">
                                    <div className="rounded-xl border p-3">
                                        <div className="text-xs text-gray-500">Complexity</div>
                                        <div className="font-medium">{selected.metrics.timeComplexityLabel}</div>
                                    </div>
                                    <div className="rounded-xl border p-3">
                                        <div className="text-xs text-gray-500">Cyclomatic</div>
                                        <div className="font-medium">{selected.metrics.cyclomaticComplexity}</div>
                                    </div>
                                    <div className="rounded-xl border p-3">
                                        <div className="text-xs text-gray-500">Robustness</div>
                                        <div className="font-medium">{selected.metrics.robustInputChecks ? "Validates inputs" : "No checks"}</div>
                                    </div>
                                    <div className="rounded-xl border p-3">
                                        <div className="text-xs text-gray-500">Edge Handling</div>
                                        <div className="font-medium">{selected.metrics.handlesNegativesAndZero ? "Negatives/Zero handled" : "Not handled"}</div>
                                    </div>
                                </div>
                                {best?.c.id === selected.id ? (
                                    <div className="mt-2 text-emerald-700 text-sm inline-flex items-center gap-1">
                                        <CheckCircle2 className="h-4 w-4" /> Auto-picked as best fit
                                    </div>
                                ) : (
                                    <div className="mt-2 text-amber-700 text-sm inline-flex items-center gap-1">
                                        <XCircle className="h-4 w-4" /> Manually overridden
                                    </div>
                                )}
                            </>
                        )}
                    </CardBox>

                    <CardBox icon={<Brain className="h-5 w-5" />} title="How to plug in your LLM / backend">
                        <ol className="list-decimal pl-5 text-sm space-y-2 text-gray-700">
                            <li>
                                Replace <code>seedFromPrimeProblem()</code> with an API call that returns
                                <code>requirements</code>, <code>tests</code>, and <code>candidates</code>.
                            </li>
                            <li>
                                Map your model outputs to the <code>Candidate</code> shape including
                                complexity metadata.
                            </li>
                            <li>
                                Optionally, run static analysis server-side to compute cyclomatic complexity
                                and robustness flags.
                            </li>
                            <li>
                                Tune <code>scoreCandidate()</code> to match your prioritization (e.g., weigh
                                performance more).
                            </li>
                        </ol>
                    </CardBox>
                </div>
            </main>

            <footer className="mx-auto max-w-7xl px-4 pb-10 text-xs text-gray-500">
                Built for a canvas-like authoring flow • Replace mocks with your generators.
            </footer>
        </div>
    );
}
