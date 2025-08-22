// Canvas Code Synthesis — JSX (React)
// ------------------------------------------------------------
// Pure JSX version (no TypeScript types) of the canvas-style webapp.
// TailwindCSS + lucide-react (icons)
// - Problem → Generated Requirements → Test Cases → Candidate Codes → Selected Code
// - "Run Tests" posts to your backend and auto-selects the best candidate
//   by pass count → fail count → complexity.
//
// Fix: removed all `import.meta` usage to avoid SyntaxError in non-module envs.
// Endpoint discovery order:
//   1) window.__TEST_API__
//   2) process.env.NEXT_PUBLIC_TEST_API (Next inlines at build time)
//   3) <meta name="test-api" content="..."> tag
//   4) fallback "/api/run-tests"
//
// + Added a Tailwind detection banner to help when the UI looks "unstyled" in some envs.
//   If Tailwind isn't active, you'll see setup instructions at the top.
//
// Usage: save as `CanvasCodeSynthesis.jsx` and import it in your app.
// Requires Tailwind in your project and (optionally) lucide-react.

import React, { useMemo, useState, useEffect } from "react";
import { Brain, FileText, Beaker, Code as CodeIcon, CheckCircle2, Sparkles, Copy as CopyIcon, ListChecks } from "lucide-react";

import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';


// --------------------------- Helpers & Data ---------------------------

const REQ_COLOR_PALETTE = [
    { bg: "bg-emerald-50", text: "text-emerald-700", border: "border-emerald-300", dot: "bg-emerald-500", ring: "ring-emerald-200" },
    { bg: "bg-sky-50", text: "text-sky-700", border: "border-sky-300", dot: "bg-sky-500", ring: "ring-sky-200" },
    { bg: "bg-amber-50", text: "text-amber-800", border: "border-amber-300", dot: "bg-amber-500", ring: "ring-amber-200" },
    { bg: "bg-violet-50", text: "text-violet-700", border: "border-violet-300", dot: "bg-violet-500", ring: "ring-violet-200" },
    { bg: "bg-rose-50", text: "text-rose-700", border: "border-rose-300", dot: "bg-rose-500", ring: "ring-rose-200" },
    { bg: "bg-teal-50", text: "text-teal-700", border: "border-teal-300", dot: "bg-teal-500", ring: "ring-teal-200" },
    { bg: "bg-lime-50", text: "text-lime-700", border: "border-lime-300", dot: "bg-lime-500", ring: "ring-lime-200" },
    { bg: "bg-fuchsia-50", text: "text-fuchsia-700", border: "border-fuchsia-300", dot: "bg-fuchsia-500", ring: "ring-fuchsia-200" },
];

const COMPLEXITY_TARGET_RANK = 3; // O(√n)

// Tailwind presence check: if tailwind isn't loaded, `hidden` won't set display:none
function useTailwindPresence() {
    const [ok, setOk] = useState(true);
    useEffect(() => {
        try {
            const el = document.createElement("div");
            el.className = "hidden";
            document.body.appendChild(el);
            const style = window.getComputedStyle(el);
            const hiddenWorks = style && style.display === "none";
            document.body.removeChild(el);
            setOk(!!hiddenWorks);
        } catch {
            setOk(true);
        }
    }, []);
    return ok;
}



function seedFromPrimeProblem(problem) {
    const requirements = [
        { id: "fr-io", kind: "functional", title: "Function takes integer n and values x, y; returns a single value.", details: ["Signature: x_or_y(n, x, y)"], mandatory: true },
        { id: "fr-behavior", kind: "functional", title: "Return x if n is prime; otherwise return y.", mandatory: true },
        { id: "fr-edges", kind: "functional", title: "Edge cases", details: ["If n < 0 => return y", "If n == 0 => return y"], mandatory: true },
        { id: "nfr-perf", kind: "nonfunctional", category: "performance", title: "Time complexity O(√ n) for primality check; responsive under 5s for huge n.", mandatory: true },
        { id: "nfr-robust", kind: "nonfunctional", category: "robustness", title: "Robustness", details: ["If n is not an integer => print error to stderr and return None", "If x or y not numeric => print error to stderr and return None"] },
        { id: "nfr-maint", kind: "nonfunctional", category: "maintainability", title: "Cyclomatic Complexity ≤ 5" },
    ];

    const tests = [
        { id: "t1", title: "Prime returns x", code: "assert x_or_y(13, 77, 2) == 77", fromReqIds: ["fr-behavior", "fr-io"] },
        { id: "t2", title: "Composite returns y", code: "assert x_or_y(24, 8, 9) == 9", fromReqIds: ["fr-behavior", "fr-io"] },
        { id: "t3", title: "Negative n returns y", code: "assert x_or_y(-7, 77, -5) == -5", fromReqIds: ["fr-edges", "fr-io"] },
        { id: "t4", title: "Zero returns y", code: "assert x_or_y(0, 77, 0) == 0", fromReqIds: ["fr-edges", "fr-io"] },
        { id: "t5", title: "Large prime", code: "assert x_or_y(2**31-1, 34, 0) == 34", fromReqIds: ["fr-behavior", "nfr-perf", "fr-io"] },
        { id: "t6", title: "Non-int n handled", code: "assert not x_or_y('invalid', 34, 0)", fromReqIds: ["nfr-robust"] },
        { id: "t7", title: "Complexity bound", code: "assert ComplexityVisitor.total_complexity('x_or_y') <= 5", fromReqIds: ["nfr-maint"] },
    ];

    const candidates = [
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
            metrics: { timeComplexityRank: 4, timeComplexityLabel: "O(n)", cyclomaticComplexity: 4, robustInputChecks: false, handlesNegativesAndZero: false, notes: ["Simple but slower primality check", "No input validation"] },
            rationale: ["Straightforward for small n", "Baseline"],
        },
        {
            id: "cand-arch-v1",
            name: "ARCHCODE v1 — √n trial division + checks",
            origin: "archcode",
            language: "python",
            code: `import sys, math

def _is_prime(n):
    if not isinstance(n, int):
        sys.stderr.write("Invalid input: n must be an integer.\n")
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
        sys.stderr.write("Invalid input: x and y must be numeric values.\n")
        return None
    prime = _is_prime(n)
    if prime is None:
        return None
    return x if prime else y
`,
            metrics: { timeComplexityRank: 3, timeComplexityLabel: "O(√n)", cyclomaticComplexity: 5, robustInputChecks: true, handlesNegativesAndZero: true, notes: ["Validates types", "Uses isqrt", "Early reject <2"] },
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
        sys.stderr.write("Invalid input: n must be an integer.\n")
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
        sys.stderr.write("Invalid input: x and y must be numeric values.\n")
        return None
    prime = _is_prime(n)
    if prime is None:
        return None
    return x if prime else y
`,
            metrics: { timeComplexityRank: 3, timeComplexityLabel: "O(√n) (6k±1)", cyclomaticComplexity: 5, robustInputChecks: true, handlesNegativesAndZero: true, notes: ["Skips multiples of 2 and 3", "Lower constant factor"] },
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
        sys.stderr.write("Invalid input: n must be an integer.\n")
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
        sys.stderr.write("Invalid input: x and y must be numeric values.\n")
        return None
    prime = _is_prime(n)
    if prime is None:
        return None
    return x if prime else y
`,
            metrics: { timeComplexityRank: 2, timeComplexityLabel: "O(k·log^3 n) (prob.)", cyclomaticComplexity: 7, robustInputChecks: true, handlesNegativesAndZero: true, notes: ["Probabilistic test with fixed bases", "Very fast for large n"] },
            rationale: ["Fast probabilistic check for very large n"],
        },
    ];

    return { problem, requirements, tests, candidates };
}

function scoreCandidate(c, reqs) {
    let score = 0;
    const reasons = [];
    let functionalOK = true;

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

    if (c.metrics.timeComplexityRank <= COMPLEXITY_TARGET_RANK) {
        score += 20;
        reasons.push(`Meets complexity target (${c.metrics.timeComplexityLabel})`);
    } else {
        reasons.push(`Slower than target (${c.metrics.timeComplexityLabel})`);
    }

    const wantsRobustness = reqs.some((r) => r.id === "nfr-robust");
    if (wantsRobustness && c.metrics.robustInputChecks) {
        score += 15;
        reasons.push("Has input validations (robustness)");
    }

    const wantsMaintainability = reqs.some((r) => r.id === "nfr-maint");
    if (wantsMaintainability && c.metrics.cyclomaticComplexity <= 5) {
        score += 10;
        reasons.push("Cyclomatic complexity ≤ 5");
    }

    score += Math.max(0, 10 - c.metrics.cyclomaticComplexity);
    if (c.rationale?.length) score += 5;

    return { score, reasons, ok: functionalOK };
}

// --------------------------- Small UI bits ---------------------------

function Badge({ children, className = "" }) {
    return (
        <span className={`inline-flex items-center rounded-full border px-2 py-0.5 text-xs font-medium text-gray-600 ${className}`}>
      {children}
    </span>
    );
}

function CardBox({ icon, title, right, children }) {
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

function MonoBlock({ code, className }) {
    return (
    <pre className={`rounded-xl border bg-white-900 text-neutral-200 overflow-auto p-4 text-sm leading-relaxed ${className ?? ""}`}>
        <SyntaxHighlighter language="python" style={docco}>
            {code}
        </SyntaxHighlighter>
    </pre>
    );
}

function CopyButton({ text }) {
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

// --------------------------- Main Component ---------------------------

function getTestApiEndpoint() {
    try {
        if (typeof window !== "undefined" && window.__TEST_API__) return window.__TEST_API__;
    } catch {}
    try {
        // Next.js will inline this at build time on the client bundle
        if (typeof process !== "undefined" && process.env && process.env.NEXT_PUBLIC_TEST_API) return process.env.NEXT_PUBLIC_TEST_API;
    } catch {}
    try {
        if (typeof document !== "undefined") {
            const meta = document.querySelector('meta[name="test-api"]');
            if (meta && meta.getAttribute("content")) return meta.getAttribute("content");
        }
    } catch {}
    return "/api/run-tests";
}

export default function CanvasCodeSynthesis() {
    const [problem, setProblem] = useState(
        "A simple program which should return the value of x if n is a prime number and should return the value of y otherwise."
    );
    const [bundle, setBundle] = useState(() => seedFromPrimeProblem(
        "A simple program which should return the value of x if n is a prime number and should return the value of y otherwise."
    ));

    const [selectedId, setSelectedId] = useState(null);
    const [testResults, setTestResults] = useState({}); // { [candId]: { pass, fail, total } }
    const [testBestId, setTestBestId] = useState(null);
    const [testing, setTesting] = useState(false);
    const [testError, setTestError] = useState("");

    const tailwindOK = useTailwindPresence();

    const scored = useMemo(() => {
        if (!bundle) return [];
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
        const id = (testBestId ?? selectedId) ?? best?.c.id ?? null;
        return id ? bundle.candidates.find((c) => c.id === id) ?? null : null;
    }, [bundle, best, selectedId, testBestId]);

    const reqIndexMap = useMemo(() => new Map((bundle?.requirements ?? []).map((r, i) => [r.id, i])), [bundle]);

    const colorFor = (rid) => {
        const idx = reqIndexMap.get(rid) ?? 0;
        return REQ_COLOR_PALETTE[idx % REQ_COLOR_PALETTE.length];
    };

    const reqLabel = (rid) => {
        const r = bundle?.requirements.find((x) => x.id === rid);
        if (!r) return rid;
        const prefix = r.kind === "functional" ? "FR" : "NFR";
        return `${prefix}: ${r.title}`;
    };

    function handleGenerate() {
        const p = (problem || "").trim();
        const looksPrime = /prime|\b소수\b|\bn is a prime/i.test(p);
        if (looksPrime) {
            const seeded = seedFromPrimeProblem(p);
            setBundle(seeded);
            setSelectedId(null);
            setTestResults({});
            setTestBestId(null);
            return;
        }
        const basic = {
            problem: p,
            requirements: [
                { id: "fr-1", kind: "functional", title: "Define function meeting the described behavior.", mandatory: true },
                { id: "nfr-perf", kind: "nonfunctional", category: "performance", title: "Reasonable time complexity for input size." },
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
                    metrics: { timeComplexityRank: 4, timeComplexityLabel: "O(n)", cyclomaticComplexity: 4, robustInputChecks: false, handlesNegativesAndZero: false },
                },
            ],
        };
        setBundle(basic);
        setSelectedId(null);
        setTestResults({});
        setTestBestId(null);
    }

    async function handleRunTests() {
        if (!bundle) return;
        setTestError("");
        try {
            setTesting(true);
            const endpoint = getTestApiEndpoint();
            const res = await fetch(endpoint, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    problem: bundle.problem,
                    requirements: bundle.requirements,
                    tests: bundle.tests,
                    candidates: bundle.candidates.map(({ id, name, code, language }) => ({ id, name, code, language })),
                }),
            });
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const data = await res.json();
            const results = data?.results || {};
            setTestResults(results);
            const entries = Object.entries(results);
            if (entries.length) {
                const cmap = new Map(bundle.candidates.map((c) => [c.id, c]));
                entries.sort((a, b) => {
                    const ar = a[1], br = b[1];
                    if (br.pass !== ar.pass) return br.pass - ar.pass;
                    if (ar.fail !== br.fail) return ar.fail - br.fail;
                    const ca = cmap.get(a[0]); const cb = cmap.get(b[0]);
                    return ca.metrics.timeComplexityRank - cb.metrics.timeComplexityRank;
                });
                const bestId = entries[0][0];
                setTestBestId(bestId);
                setSelectedId(bestId);
            }
        } catch (e) {
            console.error("run-tests error", e);
            setTestError(String(e?.message || e));
        } finally {
            setTesting(false);
        }
    }

    const totalTests = bundle?.tests.length ?? 0;

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 text-slate-900">

            <div className="max-w-6xl mx-auto px-4 py-6 space-y-6">
                {/* Problem */}
                <CardBox
                    icon={<FileText className="h-5 w-5" />}
                    title="1) Problem Description"
                    right={
                        <div className="flex items-center gap-2">
                            <button onClick={handleGenerate} className="inline-flex items-center gap-2 rounded-2xl border px-3 py-1.5 text-sm hover:bg-gray-50">
                                <Brain className="h-4 w-4" /> Generate
                            </button>
                            <button onClick={handleRunTests} disabled={testing || !bundle} className="inline-flex items-center gap-2 rounded-2xl border px-3 py-1.5 text-sm hover:bg-gray-50 disabled:opacity-50">
                                <Beaker className="h-4 w-4" /> {testing ? "Testing..." : "Run Tests"}
                            </button>
                        </div>
                    }
                >
          <textarea
              value={problem}
              onChange={(e) => setProblem(e.target.value)}
              placeholder="Describe what the program must do..."
              className="w-full rounded-xl border px-3 py-2 bg-white focus:outline-none focus:ring-2 ring-violet-200"
              rows={5}
          />
                    <p className="text-xs text-slate-500 mt-2">Tip: If it mentions primes/소수, a rich example will load.</p>
                    {testError ? (
                        <div className="mt-3 text-sm text-rose-700 bg-rose-50 border border-rose-200 rounded-lg px-3 py-2">
                            Test error: {testError}
                        </div>
                    ) : null}
                </CardBox>

                {/* Requirements */}
                <CardBox icon={<ListChecks className="h-5 w-5" />} title="2) Generated Requirements">
                    <div className="space-y-3">
                        <div className="text-[11px] uppercase tracking-wider text-slate-500">Functional</div>
                        <div className="grid gap-2">
                            {(bundle?.requirements || []).filter((r) => r.kind === "functional").map((r) => {
                                const c = colorFor(r.id);
                                return (
                                    <div key={r.id} className={`flex items-start gap-2 rounded-lg border p-2 ${c.bg}`}>
                                        <span className={`mt-1 h-2 w-2 rounded-full ${c.dot}`} />
                                        <div>
                                            <div className="font-medium">{r.title}</div>
                                            {r.details?.length ? (
                                                <ul className="list-disc pl-5 text-sm text-slate-600 mt-1">
                                                    {r.details.map((d, i) => (<li key={i}>{d}</li>))}
                                                </ul>
                                            ) : null}
                                        </div>
                                    </div>
                                );
                            })}
                        </div>

                        <div className="text-[11px] uppercase tracking-wider text-slate-500 mt-3">Non-Functional</div>
                        <div className="grid gap-2">
                            {(bundle?.requirements || []).filter((r) => r.kind === "nonfunctional").map((r) => {
                                const c = colorFor(r.id);
                                return (
                                    <div key={r.id} className={`flex items-start gap-2 rounded-lg border p-2 ${c.bg}`}>
                                        <span className={`mt-1 h-2 w-2 rounded-full ${c.dot}`} />
                                        <div>
                                            <div className="font-medium">{r.title}</div>
                                            {r.details?.length ? (
                                                <ul className="list-disc pl-5 text-sm text-slate-600 mt-1">
                                                    {r.details.map((d, i) => (<li key={i}>{d}</li>))}
                                                </ul>
                                            ) : null}
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                </CardBox>

                {/* Tests */}
                <CardBox icon={<Beaker className="h-5 w-5" />} title="3) Generated Test Cases">
                    <div className="space-y-2">
                        {(bundle?.tests || []).map((t) => (
                            <div key={t.id} className="rounded-xl border p-3 bg-white">
                                <div className="font-medium">{t.title}</div>
                                {t.fromReqIds?.length ? (
                                    <div className="flex flex-wrap gap-1 mt-1">
                                        {t.fromReqIds.map((rid) => {
                                            const c = colorFor(rid);
                                            return (
                                                <Badge key={rid} className={`${c.bg} ${c.text} ${c.border}`}>
                                                    {reqLabel(rid)}
                                                </Badge>
                                            );
                                        })}
                                    </div>
                                ) : null}
                                <MonoBlock code={t.code} className="mt-2" />
                            </div>
                        ))}
                    </div>
                </CardBox>

                {/* Candidates */}
                <CardBox icon={<CodeIcon className="h-5 w-5" />} title="4) Candidate Codes">
                    <div className="space-y-4">
                        {(bundle?.candidates || []).map((c) => {
                            const { score, ok } = scoreCandidate(c, bundle.requirements);
                            const tests = testResults[c.id];
                            const selectedStyle = selected?.id === c.id ? "border-violet-400" : "border-slate-200";
                            return (
                                <div key={c.id} className={`rounded-2xl border p-3 ${selectedStyle}`}>
                                    <div className="flex items-start justify-between gap-3">
                                        <div>
                                            <div className="font-medium">{c.name}</div>
                                            <div className="text-xs text-slate-500 flex items-center gap-2">
                                                <span>{(c.language || "").toUpperCase()}</span>
                                                {c.origin === "archcode" ? <Badge className="bg-indigo-50 text-indigo-700 border-indigo-300">ARCHCODE</Badge> : null}
                                            </div>
                                        </div>
                                        <div className="text-right text-xs">
                                            <div>Score: <span className="font-semibold">{score}</span></div>
                                            <div className={ok ? "text-emerald-600" : "text-amber-600"}>{ok ? "Meets" : "May violate"} required FRs</div>
                                            <div className="mt-1">Tests: <span className="font-semibold">{(tests?.pass ?? 0)}/{(tests?.total ?? totalTests)}</span></div>
                                        </div>
                                    </div>

                                    <div className="flex flex-wrap gap-2 mt-2">
                                        <Badge>Complexity: {c.metrics.timeComplexityLabel}</Badge>
                                        <Badge>CC: {c.metrics.cyclomaticComplexity}</Badge>
                                        <Badge>{c.metrics.robustInputChecks ? "Robust" : "No checks"}</Badge>
                                        <Badge>{c.metrics.handlesNegativesAndZero ? "Edge-safe" : "Edge-unsafe"}</Badge>
                                    </div>

                                    {c.metrics?.notes?.length ? (
                                        <ul className="list-disc pl-5 text-sm text-slate-600 mt-2">
                                            {c.metrics.notes.map((n, i) => (<li key={i}>{n}</li>))}
                                        </ul>
                                    ) : null}

                                    <MonoBlock code={c.code} className="mt-2" />

                                    <div className="flex items-center justify-between mt-2">
                                        <button onClick={() => setSelectedId(c.id)} className="inline-flex items-center gap-2 rounded-xl border px-3 py-1.5 text-sm hover:bg-gray-50">
                                            <CheckCircle2 className="h-4 w-4" /> Use this
                                        </button>
                                        <CopyButton text={c.code} />
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </CardBox>

                {/* Selected */}
                <CardBox icon={<CheckCircle2 className="h-5 w-5" />} title="5) Selected Code">
                    {!selected ? (
                        <div className="text-slate-500 text-sm">No selection. Generate and pick a candidate or run tests.</div>
                    ) : (
                        <div className="space-y-3">
                            <div className="flex items-center justify-between">
                                <div>
                                    <div className="text-xs uppercase tracking-wider text-slate-500">Chosen Candidate</div>
                                    <div className="font-semibold text-lg">{selected.name}</div>
                                </div>
                                <CopyButton text={selected.code} />
                            </div>
                            <MonoBlock code={selected.code} />
                            <div className="grid grid-cols-2 gap-2">
                                <div className="rounded-xl border p-3"><div className="text-xs text-slate-500">Complexity</div><div className="font-medium">{selected.metrics.timeComplexityLabel}</div></div>
                                <div className="rounded-xl border p-3"><div className="text-xs text-slate-500">Cyclomatic</div><div className="font-medium">{selected.metrics.cyclomaticComplexity}</div></div>
                                <div className="rounded-xl border p-3"><div className="text-xs text-slate-500">Robust</div><div className="font-medium">{selected.metrics.robustInputChecks ? "Yes" : "No"}</div></div>
                                <div className="rounded-xl border p-3"><div className="text-xs text-slate-500">Edge-safe</div><div className="font-medium">{selected.metrics.handlesNegativesAndZero ? "Yes" : "No"}</div></div>
                            </div>
                            {testBestId && selected.id === testBestId ? (
                                <div className="inline-flex items-center gap-2 text-emerald-700 bg-emerald-50 border border-emerald-200 rounded-full px-3 py-1 text-sm">
                                    Selected by server test results
                                </div>
                            ) : (
                                <div className="inline-flex items-center gap-2 text-amber-700 bg-amber-50 border border-amber-200 rounded-full px-3 py-1 text-sm">
                                    Manually selected
                                </div>
                            )}
                        </div>
                    )}
                </CardBox>
            </div>
        </div>
    );
}
