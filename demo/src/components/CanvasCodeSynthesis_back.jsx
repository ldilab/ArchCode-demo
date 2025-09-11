// Canvas Code Synthesis — JSX (React)
// ------------------------------------------------------------
// Pure JSX version (no TypeScript types) of the canvas-style webapp.
// TailwindCSS + lucide-react (icons) + @monaco-editor/react
// Layout: 1) Problem → 2) Tests by Requirement (left) | 3) Candidates → 4) Selected Code (right)
//
// This revision fixes:
// - Unterminated string constants in JSX and object literals
// - Regex with stray control characters (now uses proper word boundaries)
// - Ensures all JSX tags are properly closed
// - Keeps streaming /generate NDJSON integration and existing tests intact

import React, { useMemo, useState, useEffect } from "react";
import { Brain, FileText, Beaker, Code as CodeIcon, CheckCircle2, Copy as CopyIcon, Settings } from "lucide-react";
import SyntaxHighlighter from "react-syntax-highlighter";
import { docco } from "react-syntax-highlighter/dist/esm/styles/hljs";
import Editor from "@monaco-editor/react";
import LDILogo from '/ldi-logo.svg';


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
        { id: "t8", title: "One returns y (edge)", code: "assert x_or_y(1, 99, -1) == -1", fromReqIds: ["fr-edges", "fr-io"] },
        { id: "t9", title: "x/y must be numeric", code: "assert not x_or_y(5, 'nope', 0)", fromReqIds: ["nfr-robust", "fr-io"] },
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
        # (loop omitted in display-only snippet)
        return True
`,
            // NOTE: Placeholder lines are for display only and not executed; kept to show approach.
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

export default function CanvasCodeSynthesis() {
    const [problem, setProblem] = useState(
        "A simple program which should return the value of x if n is a prime number and should return the value of y otherwise."
    );
    const [bundle, setBundle] = useState(() => seedFromPrimeProblem(
        "A simple program which should return the value of x if n is a prime number and should return the value of y otherwise."
    ));

    const [selectedId, setSelectedId] = useState(null);

    const [sampleCount, setSampleCount] = useState(3);
    const [llm, setLlm] = useState({
        platform: "openai",
        model_name: "gpt-4o-mini",
        strategy: "greedy",
        kwargs: { temperature: 0.8, top_p: 1.0, max_tokens: 2048 },
    });
    const [showLlm, setShowLlm] = useState(false);

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
        const id = selectedId ?? best?.c.id ?? null;
        return id ? bundle.candidates.find((c) => c.id === id) ?? null : null;
    }, [bundle, best, selectedId]);

    const [selectedCode, setSelectedCode] = useState("");
    const [sortKey, setSortKey] = useState("score"); // 'score' | 'tests' | 'complexity'
    const [sortDir, setSortDir] = useState("desc"); // 'asc' | 'desc'
    const [filterFrMeets, setFilterFrMeets] = useState(false);
    const [streaming, setStreaming] = useState(false);

    // define totalTests before any usage
    const totalTests = bundle?.tests?.length ?? 0;

    const sortedCandidates = useMemo(() => {
        const trSource = bundle?.testResults || {};
        const decorated = (bundle?.candidates || []).map((c) => {
            const { score, ok } = scoreCandidate(c, bundle.requirements);
            const tr = trSource[c.id] || {};
            const pass = tr.pass ?? 0;
            const total = tr.total ?? totalTests;
            const fail = tr.fail ?? Math.max(0, total - pass);
            return { c, score, ok, pass, fail, total };
        });
        const filtered = filterFrMeets ? decorated.filter((d) => d.ok) : decorated;
        const s = filtered.slice();
        s.sort((a, b) => {
            if (sortKey === "score") {
                if (a.score !== b.score) return sortDir === "asc" ? a.score - b.score : b.score - a.score;
                if (a.pass !== b.pass) return b.pass - a.pass;
                const ar = a.c.metrics.timeComplexityRank, br = b.c.metrics.timeComplexityRank;
                if (ar !== br) return ar - br;
                return 0;
            } else if (sortKey === "tests") {
                if (a.pass !== b.pass) return sortDir === "asc" ? a.pass - b.pass : b.pass - a.pass;
                if (a.fail !== b.fail) return a.fail - b.fail;
                const ar = a.c.metrics.timeComplexityRank, br = b.c.metrics.timeComplexityRank;
                if (ar !== br) return ar - br;
                return b.score - a.score;
            } else { // complexity
                const ar = a.c.metrics.timeComplexityRank, br = b.c.metrics.timeComplexityRank;
                if (ar !== br) return sortDir === "asc" ? ar - br : br - ar;
                if (a.score !== b.score) return b.score - a.score;
                if (a.pass !== b.pass) return b.pass - a.pass;
                return 0;
            }
        });
        return s;
    }, [bundle, totalTests, sortKey, sortDir, filterFrMeets]);

    useEffect(() => {
        setSelectedCode(selected?.code ?? "");
    }, [selected]);

    const reqIndexMap = useMemo(() => new Map((bundle?.requirements ?? []).map((r, i) => [r.id, i])), [bundle]);

    const colorFor = (rid) => {
        const idx = reqIndexMap.get(rid) ?? 0;
        return REQ_COLOR_PALETTE[idx % REQ_COLOR_PALETTE.length];
    };

    // --- REST API helpers ---
    const buildServerLlmKwargs = (llm) => ({
        model_name: llm.model_name,
        platform: llm.platform,
        greedy_kwargs: { ...llm.kwargs },
        nucleus_kwargs: { ...llm.kwargs },
    });

    const splitLines = (val) => String(val || "")
        .split(/\r?\n/)
        .map((s) => s.trim())
        .filter(Boolean);

    const pickReqId = (reqs, preferred) => {
        const ids = new Set((reqs || []).map((r) => r.id));
        if (preferred && ids.has(preferred)) return preferred;
        if (ids.has("fr-behavior")) return "fr-behavior";
        if (ids.has("fr-1")) return "fr-1";
        return Array.from(ids)[0];
    };

    const handleStreamMessage = (msg) => {
        // 1) requirements
        if (msg.requirements || msg.requirements_raw) {
            setBundle((prev) => {
                let nextReqs = prev.requirements || [];
                if (Array.isArray(msg.requirements)) {
                    const appended = msg.requirements.map((text, i) => ({
                        id: `fr-auto-${Date.now()}-${i}`,
                        kind: "functional",
                        title: text,
                        mandatory: false,
                    }));
                    nextReqs = [...nextReqs, ...appended];
                }
                return {
                    ...prev,
                    stream: { ...(prev.stream || {}), requirements_raw: msg.requirements_raw, requirements: msg.requirements },
                    requirements: nextReqs,
                };
            });
            return;
        }

        // 2) plan
        if (msg.plan || msg.plan_raw) {
            setBundle((prev) => ({
                ...prev,
                stream: { ...(prev.stream || {}), plan_raw: msg.plan_raw, plan: msg.plan },
            }));
            return;
        }

        // 3) generated test cases grouped
        if (msg.gen_tc) {
            const catToReq = {
                edge: "fr-edges",
                performance: "nfr-perf",
                robustness: "nfr-robust",
                maintainability: "nfr-maint",
                fr: "fr-behavior",
                general: "fr-behavior",
                nfr: "nfr-perf",
                sqr: "nfr-maint",
            };
            setBundle((prev) => {
                const tests = { ...(msg.gen_tc || {}) };
                let newTests = prev.tests ? prev.tests.slice() : [];
                Object.entries(tests).forEach(([cat, body]) => {
                    const lines = splitLines(body);
                    if (!lines.length) return;
                    const rid = catToReq[cat] || pickReqId(prev.requirements);
                    lines.forEach((code, idx) => {
                        const id = `st-${cat}-${Date.now()}-${idx}`;
                        newTests.push({ id, title: `${cat.toUpperCase()} ${idx + 1}`, code, fromReqIds: rid ? [rid] : [] });
                    });
                });
                return { ...prev, tests: newTests, stream: { ...(prev.stream || {}), gen_tc: msg.gen_tc } };
            });
            return;
        }

        // 4) generated codes
        if (Array.isArray(msg.code) || Array.isArray(msg.code_raw)) {
            const codes = Array.isArray(msg.code) ? msg.code : (msg.code_raw || []);
            setBundle((prev) => {
                const baseMetrics = (prev.candidates && prev.candidates[0] && prev.candidates[0].metrics) || {
                    timeComplexityRank: 3,
                    timeComplexityLabel: "O(√n)",
                    cyclomaticComplexity: 5,
                    robustInputChecks: false,
                    handlesNegativesAndZero: false,
                    notes: [],
                };
                const newCands = codes.map((codeStr, i) => ({
                    id: `cand-${i}`,
                    name: `Candidate ${i + 1}`,
                    origin: "archcode",
                    language: "python",
                    code: String(codeStr || ""),
                    metrics: { ...baseMetrics },
                    rationale: prev.candidates?.[i]?.rationale || [],
                }));
                return {
                    ...prev,
                    candidates: newCands.length ? newCands : prev.candidates,
                    stream: { ...(prev.stream || {}), code_raw: msg.code_raw, code: msg.code },
                };
            });
            return;
        }

        // 5) execution details
        if (Array.isArray(msg.gen_tc_passed)) {
            setBundle((prev) => {
                const passed = msg.gen_tc_passed; // [[bool]]
                const mapping = {};
                passed.forEach((row, i) => {
                    const id = `cand-${i}`;
                    const total = Array.isArray(row) ? row.length : 0;
                    const pass = Array.isArray(row) ? row.filter(Boolean).length : 0;
                    const fail = Math.max(0, total - pass);
                    mapping[id] = { pass, fail, total };
                });
                return { ...prev, testResults: { ...(prev.testResults || {}), ...mapping }, stream: { ...(prev.stream || {}), gen_tc_passed: msg.gen_tc_passed } };
            });
            return;
        }

        if (Array.isArray(msg.gen_tc_exec_code) || Array.isArray(msg.gen_tc_exec_result)) {
            setBundle((prev) => ({
                ...prev,
                stream: { ...(prev.stream || {}), gen_tc_exec_code: msg.gen_tc_exec_code, gen_tc_exec_result: msg.gen_tc_exec_result },
            }));
            return;
        }
    };

    async function streamFromApi() {
        if (streaming) return;
        setStreaming(true);
        try {
            const payload = {
                nl_query: problem,
                llm_kwargs: buildServerLlmKwargs(llm),
                candidate_num: sampleCount,
            };
            const res = await fetch("/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            });
            if (!res.ok || !res.body) throw new Error(`HTTP ${res.status}`);
            const reader = res.body.getReader();
            const decoder = new TextDecoder();
            let buffer = "";
            while (true) {
                const { value, done } = await reader.read();
                if (done) break;
                buffer += decoder.decode(value, { stream: true });
                let idx;
                while ((idx = buffer.indexOf("\n")) >= 0) {
                    const line = buffer.slice(0, idx).trim();
                    buffer = buffer.slice(idx + 1);
                    if (!line) continue;
                    try { handleStreamMessage(JSON.parse(line)); } catch (e) { /* ignore partials */ }
                }
            }
            const tail = buffer.trim();
            if (tail) { try { handleStreamMessage(JSON.parse(tail)); } catch {} }
        } catch (e) {
            console.error("streamFromApi error", e);
        } finally {
            setStreaming(false);
        }
    }

    function handleGenerate() {
        const p = (problem || "").trim();
        const looksPrime = /prime|\b소수\b|\bn is a prime/i.test(p);
        if (looksPrime) {
            const seeded = seedFromPrimeProblem(p);
            const seededWithMeta = {
                ...seeded,
                samplingCount: sampleCount,
                llmParams: {
                    platform: llm.platform,
                    model_name: llm.model_name,
                    strategy: llm.strategy,
                    kwargs: llm.kwargs,
                },
            };
            setBundle(seededWithMeta);
            setSelectedId(null);
            return;
        }
        const basic = {
            problem: p,
            samplingCount: sampleCount,
            llmParams: {
                platform: llm.platform,
                model_name: llm.model_name,
                strategy: llm.strategy,
                kwargs: llm.kwargs,
            },
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
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 text-slate-900">
            <header className="sticky top-0 z-40 bg-white/70 backdrop-blur border-b">
                <div className="max-w-10xl mx-auto px-4 h-12 flex items-center">
                    <span className="text-slate-800 font-bold tracking-tight">
                        <img src={LDILogo} alt="LDI" width={30} height={30}/>
                        ARCHCODE
                    </span>
                </div>
            </header>
            <div className="max-w-6xl mx-auto px-4 py-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* LEFT COLUMN: 1~2 */}
                <div className="space-y-6">
                    {/* 1) Problem */}
                    <CardBox
                        icon={<FileText className="h-5 w-5"/>}
                        title="1) Problem Description"
                        right={
                            <div className="flex items-center gap-2">
                                <label className="flex items-center gap-2 text-sm">
                                    <span className="text-slate-600">Samples</span>
                                    <select
                                        className="border rounded-md px-2 py-1"
                                        value={sampleCount}
                                        onChange={(e) => setSampleCount(Math.max(1, parseInt(e.target.value) || 1))}
                                    >
                                        {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((n) => (
                                            <option key={n} value={n}>{n}</option>
                                        ))}
                                    </select>
                                </label>
                                <button onClick={() => setShowLlm((v) => !v)}
                                        className="inline-flex items-center gap-2 rounded-2xl border px-3 py-1.5 text-sm hover:bg-gray-50">
                                    <Settings className="h-4 w-4"/> LLM Params
                                </button>
                                <button onClick={streamFromApi} disabled={streaming}
                                        className="inline-flex items-center gap-2 rounded-2xl border px-3 py-1.5 text-sm hover:bg-gray-50 disabled:opacity-50">
                                    <Beaker className="h-4 w-4"/> {streaming ? "Streaming..." : "Stream API"}
                                </button>
                                <button onClick={handleGenerate}
                                        className="inline-flex items-center gap-2 rounded-2xl border px-3 py-1.5 text-sm hover:bg-gray-50">
                                    <Brain className="h-4 w-4"/> Generate
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
                        <p className="text-xs text-slate-500 mt-2">Tip: If it mentions primes/소수, a rich example will
                            load.</p>

                        {showLlm && (
                            <div className="mt-3 rounded-xl border bg-white p-3 space-y-3">
                                {/* Platform → Model → Decoding */}
                                <div className="grid grid-cols-1 md:grid-cols-3 gap-2">
                                    <label className="text-sm">
                                        <span className="block text-slate-600 mb-1">Platform</span>
                                        <select
                                            className="w-full border rounded-md px-2 py-1"
                                            value={llm.platform}
                                            onChange={(e) => setLlm(prev => ({...prev, platform: e.target.value}))}
                                        >
                                            <option value="openai">openai</option>
                                            <option value="azure">azure</option>
                                            <option value="anthropic">anthropic</option>
                                            <option value="other">other</option>
                                        </select>
                                    </label>
                                    <label className="text-sm">
                                        <span className="block text-slate-600 mb-1">Model</span>
                                        <input
                                            className="w-full border rounded-md px-2 py-1"
                                            value={llm.model_name}
                                            onChange={(e) => setLlm(prev => ({...prev, model_name: e.target.value}))}
                                        />
                                    </label>
                                    <label className="text-sm">
                                        <span className="block text-slate-600 mb-1">Decoding</span>
                                        <select
                                            className="w-full border rounded-md px-2 py-1"
                                            value={llm.strategy}
                                            onChange={(e) => setLlm(prev => ({...prev, strategy: e.target.value}))}
                                        >
                                            <option value="greedy">greedy</option>
                                            <option value="nucleus">nucleus</option>
                                        </select>
                                    </label>
                                </div>

                                {/* Unified kwargs */}
                                <div className="grid grid-cols-1 md:grid-cols-3 gap-2">
                                    <div className="p-2 rounded-lg border md:col-span-3">
                                        <div className="text-xs font-medium mb-1">kwargs</div>
                                        <div className="grid grid-cols-3 gap-2">
                                            <label className="text-xs">
                                                <span className="block mb-1">Temp</span>
                                                <input
                                                    type="number" step="0.01" min="0" max="2"
                                                    className="w-full border rounded-md px-2 py-1"
                                                    value={llm.kwargs.temperature}
                                                    onChange={(e) => {
                                                        const v = parseFloat(e.target.value);
                                                        if (!Number.isNaN(v)) setLlm(p => ({
                                                            ...p,
                                                            kwargs: {...p.kwargs, temperature: v}
                                                        }));
                                                    }}
                                                />
                                            </label>
                                            <label className="text-xs">
                                                <span className="block mb-1">Top_p</span>
                                                <input
                                                    type="number" step="0.01" min="0" max="1"
                                                    className="w-full border rounded-md px-2 py-1"
                                                    value={llm.kwargs.top_p}
                                                    onChange={(e) => {
                                                        const v = parseFloat(e.target.value);
                                                        if (!Number.isNaN(v)) setLlm(p => ({
                                                            ...p,
                                                            kwargs: {...p.kwargs, top_p: v}
                                                        }));
                                                    }}
                                                />
                                            </label>
                                            <label className="text-xs">
                                                <span className="block mb-1">Max tok</span>
                                                <input
                                                    type="number" step="1" min="1"
                                                    className="w-full border rounded-md px-2 py-1"
                                                    value={llm.kwargs.max_tokens}
                                                    onChange={(e) => {
                                                        const v = parseInt(e.target.value) || 0;
                                                        if (v > 0) setLlm(p => ({
                                                            ...p,
                                                            kwargs: {...p.kwargs, max_tokens: v}
                                                        }));
                                                    }}
                                                />
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}
                    </CardBox>

                    {/* 2) Tests by Requirement */}
                    <CardBox icon={<Beaker className="h-5 w-5"/>} title="2) Tests by Requirement">
                        <div className="space-y-5">
                            {/* Functional */}
                            <div>
                                <div className="text-[11px] uppercase tracking-wider text-slate-500 mb-2">Functional
                                </div>
                                <div className="space-y-3">
                                    {(bundle?.requirements || []).filter((r) => r.kind === "functional").map((r) => {
                                        const c = colorFor(r.id);
                                        const testsFor = (bundle?.tests || []).filter((t) => t.fromReqIds?.includes(r.id));
                                        return (
                                            <div key={r.id} className={`rounded-xl border p-3 ${c.bg}`}>
                                                <div className="flex items-start gap-2">
                                                    <span className={`mt-1 h-2 w-2 rounded-full ${c.dot}`}/>
                                                    <div className="flex-1">
                                                        <div className="font-medium">{r.title}</div>
                                                        {r.details?.length ? (
                                                            <ul className="list-disc pl-5 text-sm text-slate-600 mt-1">
                                                                {r.details.map((d, i) => (<li key={i}>{d}</li>))}
                                                            </ul>
                                                        ) : null}
                                                    </div>
                                                </div>

                                                <div className="mt-3 space-y-2">
                                                    {testsFor.length ? (
                                                        testsFor.map((t) => (
                                                            <div key={t.id} className="rounded-lg border bg-white p-3">
                                                                <div className="font-medium">{t.title}</div>
                                                                <MonoBlock code={t.code} className="mt-2"/>
                                                            </div>
                                                        ))
                                                    ) : (
                                                        <div className="text-sm text-slate-500 italic">No tests linked
                                                            to this requirement.</div>
                                                    )}
                                                </div>
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>

                            {/* Non-Functional */}
                            <div>
                                <div
                                    className="text-[11px] uppercase tracking-wider text-slate-500 mb-2 mt-4">Non-Functional
                                </div>
                                <div className="space-y-3">
                                    {(bundle?.requirements || []).filter((r) => r.kind === "nonfunctional").map((r) => {
                                        const c = colorFor(r.id);
                                        const testsFor = (bundle?.tests || []).filter((t) => t.fromReqIds?.includes(r.id));
                                        return (
                                            <div key={r.id} className={`rounded-xl border p-3 ${c.bg}`}>
                                                <div className="flex items-start gap-2">
                                                    <span className={`mt-1 h-2 w-2 rounded-full ${c.dot}`}/>
                                                    <div className="flex-1">
                                                        <div className="font-medium">{r.title}</div>
                                                        {r.details?.length ? (
                                                            <ul className="list-disc pl-5 text-sm text-slate-600 mt-1">
                                                                {r.details.map((d, i) => (<li key={i}>{d}</li>))}
                                                            </ul>
                                                        ) : null}
                                                    </div>
                                                </div>

                                                <div className="mt-3 space-y-2">
                                                    {testsFor.length ? (
                                                        testsFor.map((t) => (
                                                            <div key={t.id} className="rounded-lg border bg-white p-3">
                                                                <div className="font-medium">{t.title}</div>
                                                                <MonoBlock code={t.code} className="mt-2"/>
                                                            </div>
                                                        ))
                                                    ) : (
                                                        <div className="text-sm text-slate-500 italic">No tests linked
                                                            to this requirement.</div>
                                                    )}
                                                </div>
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>
                        </div>
                    </CardBox>
                </div>

                {/* RIGHT COLUMN */}
                <div className="space-y-6">
                    {/* 3) Candidates */}
                    <CardBox
                        icon={<CodeIcon className="h-5 w-5"/>}
                        title="3) Candidates"
                        right={
                            <div className="flex items-center gap-3 text-sm">
                                <label className="inline-flex items-center gap-1">
                                    <input
                                        type="checkbox"
                                        className="h-4 w-4"
                                        checked={filterFrMeets}
                                        onChange={(e) => setFilterFrMeets(e.target.checked)}
                                    />
                                    <span>FR meets only</span>
                                </label>
                                <div className="inline-flex items-center gap-1">
                                    <span>Sort</span>
                                    <select
                                        className="border rounded-md px-2 py-1"
                                        value={sortKey}
                                        onChange={(e) => setSortKey(e.target.value)}
                                    >
                                        <option value="score">Score</option>
                                        <option value="tests">Tests</option>
                                        <option value="complexity">Complexity</option>
                                    </select>
                                    <button
                                        className="border rounded-md px-2 py-1"
                                        onClick={() => setSortDir((d) => (d === "asc" ? "desc" : "asc"))}
                                        title="Toggle sort order"
                                    >
                                        {sortDir === "asc" ? "Asc" : "Desc"}
                                    </button>
                                </div>
                            </div>
                        }
                    >
                        {/* Vertical list of candidate mini-cards */}
                        <div className="max-h-[60vh] overflow-y-auto pr-1">
                            <div className="flex flex-col gap-3">
                                {sortedCandidates.map((d) => {
                                    const c = d.c;
                                    const selectedStyle = selected?.id === c.id ? "ring-2 ring-violet-300 border-violet-300" : "hover:bg-gray-50";
                                    const tagBadges = [
                                        `Lang: ${(c.language || "").toUpperCase()}`,
                                        `Complexity: ${c.metrics.timeComplexityLabel}`,
                                        `CC: ${c.metrics.cyclomaticComplexity}`,
                                        c.metrics.robustInputChecks ? "Robust" : "No checks",
                                        c.metrics.handlesNegativesAndZero ? "Edge-safe" : "Edge-unsafe",
                                    ];
                                    return (
                                        <div
                                            key={c.id}
                                            role="button"
                                            tabIndex={0}
                                            onClick={() => setSelectedId(c.id)}
                                            onKeyDown={(e) => {
                                                if (e.key === "Enter" || e.key === " ") setSelectedId(c.id);
                                            }}
                                            className={`rounded-2xl border p-3 bg-white cursor-pointer w-full ${selectedStyle}`}
                                        >
                                            <div className="flex items-start justify-between">
                                                <div>
                                                    <div className="font-semibold leading-tight">{c.name}</div>
                                                    <div
                                                        className="text-xs text-slate-500 mt-0.5">{c.origin === "archcode" ? "ARCHCODE" : "Existing"}</div>
                                                </div>
                                                <div className="text-right text-xs">
                                                    <div>Score: <span className="font-semibold">{d.score}</span></div>
                                                    <div>Tests: <span
                                                        className="font-semibold">{d.pass}/{d.total}</span></div>
                                                    <div
                                                        className={d.ok ? "text-emerald-600" : "text-amber-600"}>{d.ok ? "FR meets" : "FR may violate"}</div>
                                                </div>
                                            </div>

                                            {/* Tags aligned at bottom */}
                                            <div className="mt-2 flex flex-wrap gap-1">
                                                {tagBadges.map((t, i) => (
                                                    <Badge key={i} className="bg-slate-50 border-slate-200">
                                                        {t}
                                                    </Badge>
                                                ))}
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    </CardBox>

                    {/* 4) Selected Code */}
                    <CardBox icon={<CheckCircle2 className="h-5 w-5"/>} title="4) Selected Code">
                        {!selected ? (
                            <div className="text-slate-500 text-sm">No selection. Generate and pick a candidate.</div>
                        ) : (
                            <div className="space-y-3">
                                <div className="flex items-center justify-between">
                                    <div>
                                        <div className="text-xs uppercase tracking-wider text-slate-500">Chosen
                                            Candidate
                                        </div>
                                        <div className="font-semibold text-lg">{selected.name}</div>
                                    </div>
                                    <CopyButton text={selectedCode}/>
                                </div>
                                <div className="rounded-2xl border overflow-hidden">
                                    <Editor
                                        height="70vh"
                                        defaultLanguage={selected?.language || "python"}
                                        language={selected?.language || "python"}
                                        value={selectedCode}
                                        onChange={(v) => setSelectedCode(v ?? "")}
                                        options={{
                                            fontSize: 14,
                                            minimap: {enabled: false},
                                            scrollBeyondLastLine: false,
                                            wordWrap: "on",
                                            padding: {top: 12, bottom: 12},
                                            automaticLayout: true,
                                        }}
                                    />
                                </div>
                                <div className="grid grid-cols-2 gap-2">
                                    <div className="rounded-xl border p-3">
                                        <div className="text-xs text-slate-500">Complexity</div>
                                        <div className="font-medium">{selected.metrics.timeComplexityLabel}</div>
                                    </div>
                                    <div className="rounded-xl border p-3">
                                        <div className="text-xs text-slate-500">Cyclomatic</div>
                                        <div className="font-medium">{selected.metrics.cyclomaticComplexity}</div>
                                    </div>
                                    <div className="rounded-xl border p-3">
                                        <div className="text-xs text-slate-500">Robust</div>
                                        <div
                                            className="font-medium">{selected.metrics.robustInputChecks ? "Yes" : "No"}</div>
                                    </div>
                                    <div className="rounded-xl border p-3">
                                        <div className="text-xs text-slate-500">Edge-safe</div>
                                        <div
                                            className="font-medium">{selected.metrics.handlesNegativesAndZero ? "Yes" : "No"}</div>
                                    </div>
                                </div>
                                <div
                                    className="inline-flex items-center gap-2 text-amber-700 bg-amber-50 border border-amber-200 rounded-full px-3 py-1 text-sm">
                                    Manually selected
                                </div>
                            </div>
                        )}
                    </CardBox>
                </div>
            </div>
        </div>
    );
}
