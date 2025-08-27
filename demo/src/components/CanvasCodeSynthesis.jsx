// Canvas Code Synthesis — JSX (React)
// ------------------------------------------------------------
// Pure JSX version (no TypeScript types) of the canvas-style webapp.
// TailwindCSS + lucide-react (icons) + @monaco-editor/react
// Now uses real NDJSON streaming from REST API (no local seeding)

import React, { useMemo, useState, useEffect, useRef, useCallback } from "react";
import { Brain, FileText, Beaker, Code as CodeIcon, CheckCircle2, Copy as CopyIcon, Settings, Square as StopIcon } from "lucide-react";
import SyntaxHighlighter from "react-syntax-highlighter";
import { docco } from "react-syntax-highlighter/dist/esm/styles/hljs";
import Editor from "@monaco-editor/react";

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

// const stripFences = (s) => {
//     if (!s) return "";
//     let t = String(s).trim();
//     // ```lang ... ``` 제거
//     t = t.replace(/^```[a-zA-Z]*\s*/m, "").replace(/```$/m, "").trim();
//     return t;
// };

// 서버의 문서형 요구사항 텍스트를 우리의 요구사항 카드로 변환
function normalizeRequirementsFromServer(text) {
    const s = stripFences(text);

    // 기본 카드(우리 UI가 테스트를 잘 꽂기 위해 필요한 고정 ID들)
    const reqs = [
        { id: "fr-io", kind: "functional", title: "Input / Output", details: ["Takes integers n, x, y; returns x if prime(n) else y"], mandatory: true },
        { id: "fr-behavior", kind: "functional", title: "Behavior", details: ["Return x when n is prime; otherwise y"], mandatory: true },
        { id: "fr-edges", kind: "functional", title: "Edge cases", details: ["n < 2 → y", "n = 0 → y", "handle negatives → y"] },
        { id: "nfr-perf", kind: "nonfunctional", category: "performance", title: "Performance", details: ["Time O(√n)", "Space O(1)"] },
        { id: "nfr-robust", kind: "nonfunctional", category: "robustness", title: "Robustness", details: ["If any of n,x,y not int → print error to stderr and return None"] },
        { id: "nfr-maint", kind: "nonfunctional", category: "maintainability", title: "Maintainability", details: ["Maintainability Index ≥ 60"] },
    ];

    // 텍스트 안에 추가로 등장하는 항목을 디테일에 보강(옵션)
    if (/Space complexity:\s*O\(1\)/i.test(s)) {
        const r = reqs.find(r => r.id === "nfr-perf");
        if (r && !r.details.includes("Space O(1)")) r.details.push("Space O(1)");
    }
    if (/Time complexity:\s*O\s*\(\s*sqrt\(\s*n\s*\)\s*\)/i.test(s) || /O\(sqrt\(n\)\)/i.test(s)) {
        const r = reqs.find(r => r.id === "nfr-perf");
        if (r && !r.details.some(d => /O\(√?n\)/.test(d))) r.details.unshift("Time O(√n)");
    }
    if (/Reliability/i.test(s)) {
        reqs.push({ id: "nfr-reliability", kind: "nonfunctional", category: "reliability", title: "Reliability", details: ["Consistent prime/non-prime distinction incl. edges"] });
    }

    return reqs;
}

function groupTestsByRequirement(allTests, reqs) {
    const byReq = new Map(reqs.map(r => [r.id, { req: r, tests: [] }]));
    (allTests || []).forEach(t => {
        const links = Array.isArray(t.fromReqIds) ? t.fromReqIds : [];
        if (!links.length) return;
        links.forEach(rid => {
            if (!byReq.has(rid)) return;
            byReq.get(rid).tests.push(t);
        });
    });
    return Array.from(byReq.values());
}

function coverageBadge(count) {
    if (count === 0) return { text: "No tests", className: "bg-rose-50 border-rose-200 text-rose-700" };
    if (count <= 2) return { text: `${count} test`, className: "bg-amber-50 border-amber-200 text-amber-700" };
    return { text: `${count} tests`, className: "bg-emerald-50 border-emerald-200 text-emerald-700" };
}

// (선택) 테스트 코드 내 함수명을 UI에서 통일해서 보여주고 싶다면:
function normalizeDisplayedTestCode(code, canonicalName = "prime_or_not") {
    return String(code || "")
        .replace(/\breturn_value_based_on_prime\b/g, canonicalName)
        .replace(/\bprime_check\b/g, canonicalName)
        .replace(/\bcheck_prime_return\b/g, canonicalName);
}


const stripFences = (s) => {
    if (!s) return "";
    return String(s).trim()
        .replace(/^```[a-zA-Z]*\s*/m, "")
        .replace(/```$/m, "")
        .trim();
};

// 서버 요구사항 텍스트를 계층 트리로 파싱
function parseRequirementsHierarchy(text) {
    const s = stripFences(text).replace(/\r/g, "");
    const lines = s.split("\n");

    // 간단한 마크다운 파서: 제목 라인과 "- " 들여쓰기 단계로 트리 생성
    // 규칙
    // - 최상위 제목은 " - Problem Agnostic Requirements" 처럼 시작(혹은 "Functional Requirements")
    // - 하위는 "  - ..." 식 들여쓰기(2공백=1뎁스)로 판단
    function depthOf(line) {
        const m = line.match(/^(\s*)-\s+/);
        if (!m) return -1;
        return Math.floor((m[1] || "").length / 2); // 2공백 = 1뎁스
    }
    function contentOf(line) {
        return line.replace(/^\s*-\s+/, "").trim();
    }

    const root = { id: "root", title: "root", children: [] };
    const stack = [ { node: root, depth: -1 } ];

    lines.forEach(raw => {
        const d = depthOf(raw);
        if (d < 0) return;
        const title = contentOf(raw);
        const node = { id: `node-${Math.random().toString(36).slice(2, 8)}`, title, children: [] };
        // 스택 정리
        while (stack.length && stack[stack.length-1].depth >= d) stack.pop();
        stack[stack.length-1].node.children.push(node);
        stack.push({ node, depth: d });
    });

    return root.children; // 최상위들만 반환
}

// 트리 노드 제목 → 내부 요구사항 ID 매핑
function mapTitleToReqId(title) {
    const t = (title || "").toLowerCase();

    // 최상위 그룹
    if (t.startsWith("problem agnostic")) return "nfr-general";
    if (t.startsWith("functional requirements")) return "fr-group";
    if (t.startsWith("non-functional requirements")) return "nfr-group";

    // Functional 하위
    if (/input[-\s]?output/i.test(t)) return "fr-io";
    if (/expected behavior/i.test(t)) return "fr-behavior";
    if (/edge cases?/i.test(t)) return "fr-edges";

    // Non-functional 하위
    if (/performance/i.test(t)) return "nfr-perf";
    if (/robustness/i.test(t)) return "nfr-robust";
    if (/reliability/i.test(t)) return "nfr-reliability";
    if (/maintainability/i.test(t)) return "nfr-maint";

    return null; // 테스트 연결 없는 일반 설명 노드
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
    const { copy, copied, error } = useClipboard();
    return (
        <button
            onClick={() => copy(text)}
            className="inline-flex items-center gap-1 rounded-xl border px-2.5 py-1 text-sm hover:bg-gray-50"
            title={error ? `Copy failed: ${String(error)}` : "Copy to clipboard"}
            aria-live="polite"
        >
            <CopyIcon className="h-4 w-4" /> {copied ? "Copied!" : "Copy"}
        </button>
    );
}


export function useClipboard() {
    const [copied, setCopied] = useState(false);
    const [error, setError] = useState(null);

    const copy = useCallback(async (text) => {
        setCopied(false);
        setError(null);

        try {
            if (navigator?.clipboard?.writeText) {
                // 최신 API (보안 컨텍스트 + 유저 제스처 필요)
                await navigator.clipboard.writeText(text);
                setCopied(true);
                return true;
            }

            // ---- 폴백: 구형 브라우저 ----
            const textarea = document.createElement("textarea");
            textarea.value = text;
            // iOS 대응: 화면 밖에 두되 선택 가능해야 함
            textarea.style.position = "fixed";
            textarea.style.top = "-9999px";
            textarea.setAttribute("readonly", "");
            document.body.appendChild(textarea);
            textarea.select();
            textarea.setSelectionRange(0, text.length); // iOS

            const ok = document.execCommand("copy");
            document.body.removeChild(textarea);

            if (!ok) throw new Error("execCommand copy failed");
            setCopied(true);
            return true;
        } catch (e) {
            setError(e);
            return false;
        }
    }, []);

    return { copy, copied, error };
}

// --------------------------- Main Component ---------------------------

export default function CanvasCodeSynthesis() {
    const [problem, setProblem] = useState(
        "A simple program which should return the value of x if n is a prime number and should return the value of y otherwise."
    );

    const [bundle, setBundle] = useState({
        problem: "",
        requirements: [],
        tests: [],
        candidates: [],
        testResults: {},
        stream: {},
    });

    const [selectedId, setSelectedId] = useState(null);
    const [selectedCode, setSelectedCode] = useState("");

    const [sampleCount, setSampleCount] = useState(3);
    const [llm, setLlm] = useState({
        platform: "openai",
        model_name: "gpt-4o-mini",
        strategy: "greedy",
        kwargs: { temperature: 0.8, top_p: 1.0, max_tokens: 2048 },
    });
    const [apiKey, setApiKey] = useState("");

    const [showLlm, setShowLlm] = useState(false);

    const [sortKey, setSortKey] = useState("score");
    const [sortDir, setSortDir] = useState("desc");
    const [filterFrMeets, setFilterFrMeets] = useState(false);

    const [streaming, setStreaming] = useState(false);
    const [error, setError] = useState(null);
    const [logLines, setLogLines] = useState([]); // optional: keep last N raw lines
    const abortRef = useRef(null);

    const tailwindOK = useTailwindPresence();

    const reqIndexMap = useMemo(() => new Map((bundle?.requirements ?? []).map((r, i) => [r.id, i])), [bundle]);
    const colorFor = (rid) => {
        const idx = reqIndexMap.get(rid) ?? 0;
        return REQ_COLOR_PALETTE[idx % REQ_COLOR_PALETTE.length];
    };

    // define totalTests before any usage
    const totalTests = bundle?.tests?.length ?? 0;

    const scored = useMemo(() => {
        if (!bundle) return [];
        const trSource = bundle?.testResults || {};
        const total = bundle?.tests?.length ?? 0;
        return (bundle.candidates || []).map((c) => {
            const tr = trSource[c.id] || {};
            const pass = tr.pass ?? 0;        // 🔹 boolean 합계
            const score = pass;               // 🔹 Score = 통과 개수
            const { ok } = scoreCandidate(c, bundle.requirements); // FR 충족 여부는 그대로
            return { c, score, ok, pass, total };
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

    useEffect(() => {
        setSelectedCode(selected?.code ?? "");
    }, [selected]);

    const buildServerLlmKwargs = (llm) => ({
        model_name: llm.model_name,
        platform: llm.platform,
        // 서버 스펙상 둘 다 요구됨 — 동일 kwargs를 양쪽에 넣어줌
        greedy_kwargs: { ...llm.kwargs },
        nucleus_kwargs: { ...llm.kwargs },
    });

    const makeUID = () =>
        (typeof crypto !== "undefined" && crypto.randomUUID)
            ? crypto.randomUUID()
            : `${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;

    const handleStreamMessage = (msg) => {
        // --- REQUIREMENTS ---
        if (msg.requirements || msg.requirements_raw) {
            setBundle(prev => {
                const rawArr = Array.isArray(msg.requirements) ? msg.requirements
                    : Array.isArray(msg.requirements_raw) ? msg.requirements_raw
                        : [];
                const fullText = rawArr[0] ?? "";

                const tree = parseRequirementsHierarchy(fullText);

                // 카드형 요건 리스트도 유지 (테스트 정렬/점수 계산에 필요)
                // 트리에서 등장하는 타이틀을 기반으로 ID 세트 수집
                const idsSeen = new Set();
                function walk(nodes) {
                    nodes.forEach(n => {
                        const id = mapTitleToReqId(n.title);
                        if (id) idsSeen.add(id);
                        if (n.children?.length) walk(n.children);
                    });
                }
                walk(tree);

                // 우리 UI가 기대하는 핵심 카드들만 재구성
                const reqCatalog = [
                    { id: "fr-io", kind: "functional", title: "Input / Output", details: ["Takes integers n, x, y; returns x if prime(n), else y"], mandatory: true },
                    { id: "fr-behavior", kind: "functional", title: "Expected Behavior", details: ["Return x when n is prime; otherwise y"], mandatory: true },
                    { id: "fr-edges", kind: "functional", title: "Edge Cases", details: ["n < 2 → y", "zero/negatives → y", "x==y still returns x/y correctly"] },
                    { id: "nfr-perf", kind: "nonfunctional", category: "performance", title: "Performance", details: ["Time O(√n)", "Space O(1)"] },
                    { id: "nfr-robust", kind: "nonfunctional", category: "robustness", title: "Robustness", details: ["Non-integer n/x/y → print to stderr & return None"] },
                    { id: "nfr-reliability", kind: "nonfunctional", category: "reliability", title: "Reliability", details: ["Consistent prime/non-prime distinction incl. edges"] },
                    { id: "nfr-maint", kind: "nonfunctional", category: "maintainability", title: "Maintainability", details: ["Maintainability Index ≥ 60"] },
                ].filter(r => idsSeen.has(r.id)); // 서버 텍스트에 등장한 항목만 남김(원하면 제거)

                return {
                    ...prev,
                    requirements: reqCatalog.length ? reqCatalog : prev.requirements,
                    stream: {
                        ...(prev.stream || {}),
                        requirements_raw: rawArr,
                        requirements_text: stripFences(fullText),
                        requirements_tree: tree, // 🔹 트리를 그대로 저장
                    },
                };
            });
            return;
        }

        // --- PLAN ---
        if (msg.plan || msg.plan_raw) {
            // 둘 다 배열 — UI에 보기 좋게 합쳐 저장
            const plan = Array.isArray(msg.plan) ? msg.plan : [];
            const planRaw = Array.isArray(msg.plan_raw) ? msg.plan_raw : [];
            setBundle(prev => ({
                ...prev,
                stream: {
                    ...(prev.stream || {}),
                    plan: plan.map(stripFences),
                    plan_raw: planRaw.map(stripFences),
                },
            }));
            return;
        }

        // --- GENERATED TEST CASES (gen_tc) ---
        if (msg.gen_tc || msg.gen_tc_raw) {
            const body = Array.isArray(msg.gen_tc) ? (msg.gen_tc[0] || {}) : (msg.gen_tc || {});
            const rawArr = Array.isArray(msg.gen_tc_raw) ? msg.gen_tc_raw : [];
            const rawText = rawArr[0] ? stripFences(rawArr[0]) : "";

            const catToReq = {
                edge: "fr-edges",
                performance: "nfr-perf",
                robustness: "nfr-robust",
                maintainability: "nfr-maint",
                fr: "fr-behavior",
                general: "fr-behavior",
                nfr: "nfr-robust",
                sqr: "nfr-maint",
            };

            setBundle(prev => {
                const newTests = prev.tests ? prev.tests.slice() : [];
                Object.entries(body).forEach(([cat, chunk]) => {
                    if (!chunk || !String(chunk).trim()) return; // 빈 카테고리 스킵
                    const rid = catToReq[cat] || "fr-behavior";
                    const joined = stripFences(chunk).split(/\n{2,}/).map(s => s.trim()).filter(Boolean);
                    (joined.length ? joined : [stripFences(chunk)]).forEach((code, idx) => {
                        const payload = code.includes("assert") || code.includes("try:") ? code : stripFences(chunk);
                        if (!payload.trim()) return;
                        const id = `st-${cat}-${makeUID()}`;
                        newTests.push({ id, title: `${cat.toUpperCase()} ${idx + 1}`, code: payload, fromReqIds: [rid] });
                    });
                });

                return {
                    ...prev,
                    tests: newTests,
                    stream: {
                        ...(prev.stream || {}),
                        gen_tc: msg.gen_tc,
                        gen_tc_raw: rawArr,                 // 원문 배열 보관
                        gen_tc_raw_text: rawText || null,   // 🔹 하단 폴백용 문자열
                    },
                };
            });
            return;
        }

        // --- CODE CANDIDATES ---
        if (Array.isArray(msg.code) || Array.isArray(msg.code_raw)) {
            const codes = Array.isArray(msg.code) ? msg.code : (msg.code_raw || []).map(stripFences);
            setBundle(prev => {
                const baseMetrics = {
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
                    rationale: [],
                }));
                return {
                    ...prev,
                    candidates: newCands.length ? newCands : prev.candidates,
                    stream: { ...(prev.stream || {}), code_raw: msg.code_raw, code: msg.code },
                };
            });
            return;
        }

        // --- EXEC DETAILS ---
        if (Array.isArray(msg.gen_tc_exec_code) || Array.isArray(msg.gen_tc_exec_result)) {
            setBundle(prev => ({
                ...prev,
                stream: {
                    ...(prev.stream || {}),
                    gen_tc_exec_code: msg.gen_tc_exec_code,
                    gen_tc_exec_result: msg.gen_tc_exec_result,
                },
            }));
            return;
        }

        // --- PASS MATRIX ---
        if (Array.isArray(msg.gen_tc_passed)) {
            setBundle(prev => {
                const passed = msg.gen_tc_passed; // [[bool]]
                const mapping = {};
                passed.forEach((row, i) => {
                    const id = `cand-${i}`;
                    const total = Array.isArray(row) ? row.length : 0;
                    const pass = Array.isArray(row) ? row.filter(Boolean).length : 0;
                    const fail = Math.max(0, total - pass);
                    mapping[id] = { pass, fail, total };
                });
                return {
                    ...prev,
                    testResults: { ...(prev.testResults || {}), ...mapping },
                    stream: { ...(prev.stream || {}), gen_tc_passed: msg.gen_tc_passed },
                };
            });
            return;
        }
    };


    const sortedCandidates = useMemo(() => {
        const trSource = bundle?.testResults || {};
        const decorated = (bundle?.candidates || []).map((c) => {
            const tr = trSource[c.id] || {};
            const pass = tr.pass ?? 0;
            const total = tr.total ?? totalTests;
            const fail = tr.fail ?? Math.max(0, total - pass);
            const score = pass; // 🔹 Score = 통과 개수
            const { ok } = scoreCandidate(c, bundle.requirements);
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
            } else {
                const ar = a.c.metrics.timeComplexityRank, br = b.c.metrics.timeComplexityRank;
                if (ar !== br) return sortDir === "asc" ? ar - br : br - ar;
                if (a.score !== b.score) return b.score - a.score;
                if (a.pass !== b.pass) return b.pass - a.pass;
                return 0;
            }
        });

        return s;
    }, [bundle, totalTests, sortKey, sortDir, filterFrMeets]);

    // ---- Streaming from server ----
    async function streamFromApi() {
        if (streaming) return;
        setStreaming(true);
        setError(null);
        setSelectedId(null);
        setBundle({
            problem: problem.trim(),
            requirements: [],
            tests: [],
            candidates: [],
            testResults: {},
            stream: {},
        });
        setLogLines([]);

        const payload = {
            nl_query: problem.trim(),
            llm_kwargs: buildServerLlmKwargs(llm),
            candidate_num: sampleCount,
            api_key: apiKey || undefined,
        };

        const controller = new AbortController();
        abortRef.current = controller;

        try {
            console.log(import.meta.env.VITE_API_URL)
            const res = await fetch(`${import.meta.env.VITE_API_URL}/generate`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
                signal: controller.signal,
                mode: "cors", // 필요 시 CORS 설정
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

                    // (선택) 로그에 보관 — 최근 100줄
                    setLogLines((prev) => {
                        const next = [...prev, line];
                        if (next.length > 100) next.shift();
                        return next;
                    });

                    try {
                        const msg = JSON.parse(line);
                        handleStreamMessage(msg);
                    } catch {
                        // 부분 청크/불완전 라인 무시
                    }
                }
            }
            const tail = buffer.trim();
            if (tail) {
                setLogLines((prev) => [...prev, tail].slice(-100));
                try {
                    handleStreamMessage(JSON.parse(tail));
                } catch {}
            }
        } catch (e) {
            if (e.name === "AbortError") {
                // 사용자가 중단
            } else {
                setError(String(e?.message || e));
                console.error("streamFromApi error", e);
            }
        } finally {
            setStreaming(false);
            abortRef.current = null;
        }
    }

    function stopStreaming() {
        if (abortRef.current) {
            abortRef.current.abort();
        }
    }

    function handleGenerate() {
        // 이제는 항상 서버 스트림을 사용
        streamFromApi();
    }

    const _stripFencesLocal = (s) => {
        if (!s) return "";
        let t = String(s).trim();
        // 앞/뒤 코드펜스 제거
        t = t.replace(/^```[a-zA-Z]*\s*/m, "");
        t = t.replace(/```$/m, "");
        return t.trim();
    };

    const groupTestsByRequirement = (allTests, reqs) => {
        const byReq = new Map((reqs || []).map(r => [r.id, { req: r, tests: [] }]));
        (allTests || []).forEach(t => {
            const links = Array.isArray(t.fromReqIds) ? t.fromReqIds : [];
            links.forEach(rid => {
                if (byReq.has(rid)) byReq.get(rid).tests.push(t);
            });
        });
        // reqs에 정의된 순서를 유지
        return (reqs || []).map(r => byReq.get(r.id) || { req: r, tests: [] });
    };

    const coverageBadge = (count) => {
        if (count === 0) return { text: "No tests", className: "bg-rose-50 border-rose-200 text-rose-700" };
        if (count <= 2) return { text: `${count} test`, className: "bg-amber-50 border-amber-200 text-amber-700" };
        return { text: `${count} tests`, className: "bg-emerald-50 border-emerald-200 text-emerald-700" };
    };

    const normalizeDisplayedTestCode = (code) => {
        // UI 표기용 함수명 통일 (원본은 유지됨)
        return String(code || "")
            .replace(/\breturn_value_based_on_prime\b/g, "prime_or_not")
            .replace(/\bprime_check\b/g, "prime_or_not")
            .replace(/\bcheck_prime_return\b/g, "prime_or_not");
    };

// gen_tc_raw 폴백 문자열
    const rawGenTcText =
        (bundle?.stream?.gen_tc_raw_text)
            ? bundle.stream.gen_tc_raw_text
            : Array.isArray(bundle?.stream?.gen_tc_raw) && bundle.stream.gen_tc_raw.length
                ? _stripFencesLocal(bundle.stream.gen_tc_raw[0])
                : "";

// 기능/비기능 그룹 미리 계산 (hasEmptyCategory 판별용)
    const functionalGroups = groupTestsByRequirement(
        bundle?.tests || [],
        (bundle?.requirements || []).filter(r => r.kind === "functional")
    );
    const nonfunctionalGroups = groupTestsByRequirement(
        bundle?.tests || [],
        (bundle?.requirements || []).filter(r => r.kind === "nonfunctional")
    );
    const hasEmptyCategory = [...functionalGroups, ...nonfunctionalGroups].some(g => (g.tests || []).length === 0);




    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 text-slate-900">
            <header className="sticky top-0 z-40 bg-white/70 backdrop-blur border-b">
                <div className="max-w-6xl mx-auto px-4 h-12 flex items-center justify-between">
                    <span className="text-slate-800 font-bold tracking-tight">
                        <img src="/ldi-logo.svg" width={30} height={30} />
                        ARCHCODE
                    </span>
                    <div className="flex items-center gap-2">
                        {streaming ? (
                            <span className="inline-flex items-center gap-2 text-xs text-violet-700 bg-violet-50 border border-violet-200 px-2 py-1 rounded-full">
                <span className="h-2 w-2 rounded-full bg-violet-500 animate-pulse" /> Streaming…
              </span>
                        ) : (
                            <span className="text-xs text-slate-500">Idle</span>
                        )}
                    </div>
                </div>
            </header>

            <div className="max-w-6xl mx-auto px-4 py-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* LEFT COLUMN: 1~2 */}
                <div className="space-y-6">
                    {/* 1) Problem */}
                    <CardBox
                        icon={<FileText className="h-5 w-5" />}
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
                                        {[1,2,3,4,5,6,7,8,9,10].map((n) => (
                                            <option key={n} value={n}>{n}</option>
                                        ))}
                                    </select>
                                </label>
                                <button onClick={() => setShowLlm((v) => !v)} className="inline-flex items-center gap-2 rounded-2xl border px-3 py-1.5 text-sm hover:bg-gray-50">
                                    <Settings className="h-4 w-4" /> Params
                                </button>

                                {!streaming ? (
                                    <button onClick={handleGenerate} className="inline-flex items-center gap-2 rounded-2xl border px-3 py-1.5 text-sm hover:bg-gray-50">
                                        <Brain className="h-4 w-4" /> Generate
                                    </button>
                                ) : (
                                    <button onClick={stopStreaming} className="inline-flex items-center gap-2 rounded-2xl border px-3 py-1.5 text-sm hover:bg-rose-50 border-rose-200 text-rose-700">
                                        <StopIcon className="h-4 w-4" /> Stop
                                    </button>
                                )}
                            </div>
                        }
                    >
            <textarea
                value={problem}
                onChange={(e) => setProblem(e.target.value)}
                placeholder="Describe what the program must do..."
                className="w-full rounded-xl border px-3 py-2 bg-white focus:outline-none focus:ring-2 ring-violet-200"
                rows={5}
                disabled={streaming}
            />
                        <p className="text-xs text-slate-500 mt-2">
                            Click “Generate” to stream from <span className="font-mono">/generate</span>. Responses are parsed line-by-line (NDJSON).
                        </p>

                        {showLlm && (
                            <div className="mt-3 rounded-xl border bg-white p-3 space-y-3">
                                {/* API Key */}
                                <div>
                                    <label className="text-sm block mb-1 text-slate-600">API Key</label>
                                    <input
                                        type="password"
                                        placeholder="Enter your API key"
                                        className="w-full border rounded-md px-2 py-1"
                                        value={apiKey}
                                        onChange={(e) => setApiKey(e.target.value)}
                                    />
                                </div>

                                {/* Platform → Model → Decoding */}
                                <div className="grid grid-cols-1 md:grid-cols-3 gap-2">
                                    <label className="text-sm">
                                        <span className="block text-slate-600 mb-1">Platform</span>
                                        <select
                                            className="w-full border rounded-md px-2 py-1"
                                            value={llm.platform}
                                            onChange={(e) => setLlm(prev => ({ ...prev, platform: e.target.value }))}
                                        >
                                            <option value="openai">openai</option>
                                            <option disabled value="azure">azure</option>
                                            <option disabled value="anthropic">anthropic</option>
                                            <option disabled value="other">other</option>
                                        </select>
                                    </label>
                                    <label className="text-sm">
                                        <span className="block text-slate-600 mb-1">Model</span>
                                        <input
                                            className="w-full border rounded-md px-2 py-1"
                                            value={llm.model_name}
                                            onChange={(e) => setLlm(prev => ({ ...prev, model_name: e.target.value }))}
                                        />
                                    </label>
                                    <label className="text-sm">
                                        <span className="block text-slate-600 mb-1">Decoding</span>
                                        <select
                                            className="w-full border rounded-md px-2 py-1"
                                            value={llm.strategy}
                                            onChange={(e) => setLlm(prev => ({ ...prev, strategy: e.target.value }))}
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
                                                    onChange={(e) => { const v = parseFloat(e.target.value); if (!Number.isNaN(v)) setLlm(p => ({ ...p, kwargs: { ...p.kwargs, temperature: v } })); }}
                                                />
                                            </label>
                                            <label className="text-xs">
                                                <span className="block mb-1">Top_p</span>
                                                <input
                                                    type="number" step="0.01" min="0" max="1"
                                                    className="w-full border rounded-md px-2 py-1"
                                                    value={llm.kwargs.top_p}
                                                    onChange={(e) => { const v = parseFloat(e.target.value); if (!Number.isNaN(v)) setLlm(p => ({ ...p, kwargs: { ...p.kwargs, top_p: v } })); }}
                                                />
                                            </label>
                                            <label className="text-xs">
                                                <span className="block mb-1">Max tok</span>
                                                <input
                                                    type="number" step="1" min="1"
                                                    className="w-full border rounded-md px-2 py-1"
                                                    value={llm.kwargs.max_tokens}
                                                    onChange={(e) => { const v = parseInt(e.target.value) || 0; if (v > 0) setLlm(p => ({ ...p, kwargs: { ...p.kwargs, max_tokens: v } })); }}
                                                />
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}

                        {error && (
                            <div className="mt-3 text-sm text-rose-700 bg-rose-50 border border-rose-200 rounded-xl p-2">
                                Error: {error}
                            </div>
                        )}
                        {!!logLines.length && (
                            <details className="mt-3">
                                <summary className="text-sm text-slate-600 cursor-pointer">Stream log (last {logLines.length} lines)</summary>
                                <pre className="mt-2 text-xs bg-slate-50 border rounded-lg p-2 max-h-40 overflow-auto">
{logLines.join("\n")}
                </pre>
                            </details>
                        )}
                    </CardBox>


                    {/* 2) Tests & Coverage */}
                    <CardBox icon={<Beaker className="h-5 w-5" />} title="2) Tests & Coverage (by Requirement)">
                        {/* 서버 원문 요구사항 미리보기 */}
                        {Array.isArray(bundle?.stream?.requirements) && bundle.stream.requirements[0] && (
                            <details className="mb-3">
                                <summary className="text-sm text-slate-600 cursor-pointer">View raw requirements</summary>
                                <MonoBlock className="mt-2" code={bundle.stream.requirements[0]} />
                            </details>
                        )}

                        {/* 커버리지 그리드 */}
                        <div className="space-y-5">
                            {/* Functional */}
                            <div>
                                <div className="text-[11px] uppercase tracking-wider text-slate-500 mb-2">Functional</div>
                                <div className="space-y-3">
                                    {functionalGroups.map(({ req, tests }) => {
                                        const c = colorFor(req.id);
                                        const cov = coverageBadge(tests.length);
                                        return (
                                            <div key={req.id} className={`rounded-xl border p-3 ${c.bg}`}>
                                                <div className="flex items-start justify-between gap-2">
                                                    <div className="flex items-start gap-2">
                                                        <span className={`mt-1 h-2 w-2 rounded-full ${c.dot}`} />
                                                        <div>
                                                            <div className="font-medium">{req.title}</div>
                                                            {Array.isArray(req.details) && req.details.length > 0 && (
                                                                <ul className="list-disc pl-5 text-sm text-slate-600 mt-1">
                                                                    {req.details.map((d, i) => (<li key={i}>{d}</li>))}
                                                                </ul>
                                                            )}
                                                        </div>
                                                    </div>
                                                    <span className={`inline-flex items-center rounded-full border px-2 py-0.5 text-xs font-medium ${cov.className}`}>{cov.text}</span>
                                                </div>

                                                <div className="mt-3 space-y-2">
                                                    {tests.length ? (
                                                        tests.map((t) => (
                                                            <div key={t.id} className="rounded-lg border bg-white p-3">
                                                                <div className="font-medium">{t.title}</div>
                                                                <MonoBlock code={normalizeDisplayedTestCode(t.code)} className="mt-2" />
                                                            </div>
                                                        ))
                                                    ) : (
                                                        <div className="text-sm text-slate-500 italic">No tests linked to this requirement.</div>
                                                    )}
                                                </div>
                                            </div>
                                        );
                                    })}

                                    {(bundle?.requirements || []).some(r => r.kind === "functional") ? null : (
                                        <div className="text-sm text-slate-500 italic">No functional requirements parsed yet.</div>
                                    )}
                                </div>
                            </div>

                            {/* Non-Functional */}
                            <div>
                                <div className="text-[11px] uppercase tracking-wider text-slate-500 mb-2 mt-4">Non-Functional</div>
                                <div className="space-y-3">
                                    {nonfunctionalGroups.map(({ req, tests }) => {
                                        const c = colorFor(req.id);
                                        const cov = coverageBadge(tests.length);
                                        return (
                                            <div key={req.id} className={`rounded-xl border p-3 ${c.bg}`}>
                                                <div className="flex items-start justify-between gap-2">
                                                    <div className="flex items-start gap-2">
                                                        <span className={`mt-1 h-2 w-2 rounded-full ${c.dot}`} />
                                                        <div>
                                                            <div className="font-medium">{req.title}</div>
                                                            {Array.isArray(req.details) && req.details.length > 0 && (
                                                                <ul className="list-disc pl-5 text-sm text-slate-600 mt-1">
                                                                    {req.details.map((d, i) => (<li key={i}>{d}</li>))}
                                                                </ul>
                                                            )}
                                                        </div>
                                                    </div>
                                                    <span className={`inline-flex items-center rounded-full border px-2 py-0.5 text-xs font-medium ${cov.className}`}>{cov.text}</span>
                                                </div>

                                                <div className="mt-3 space-y-2">
                                                    {tests.length ? (
                                                        tests.map((t) => (
                                                            <div key={t.id} className="rounded-lg border bg-white p-3">
                                                                <div className="font-medium">{t.title}</div>
                                                                <MonoBlock code={normalizeDisplayedTestCode(t.code)} className="mt-2" />
                                                            </div>
                                                        ))
                                                    ) : (
                                                        <div className="text-sm text-slate-500 italic">No tests linked to this requirement.</div>
                                                    )}
                                                </div>
                                            </div>
                                        );
                                    })}

                                    {(bundle?.requirements || []).some(r => r.kind === "nonfunctional") ? null : (
                                        <div className="text-sm text-slate-500 italic">No non-functional requirements parsed yet.</div>
                                    )}
                                </div>
                            </div>
                        </div>

                        {/* 🔻 폴백: 카테고리 중 하나라도 테스트가 없으면 gen_tc_raw 를 코드블록으로 하단에 출력 */}
                        {hasEmptyCategory && rawGenTcText ? (
                            <div className="mt-4">
                                <div className="text-xs uppercase tracking-wider text-slate-500 mb-1">
                                    Fallback: Raw generated tests
                                </div>
                                <MonoBlock code={rawGenTcText} />
                            </div>
                        ) : null}
                    </CardBox>

                    {/* Plans */}
                    <CardBox icon={<FileText className="h-5 w-5" />} title="Plan">
                        {Array.isArray(bundle?.stream?.plan) && bundle.stream.plan.length ? (
                            <div className="space-y-2">
                                {bundle.stream.plan.map((p, i) => (
                                    <MonoBlock key={i} code={p} />
                                ))}
                            </div>
                        ) : (
                            <div className="text-sm text-slate-500 italic">No plan received yet.</div>
                        )}
                    </CardBox>

                </div>



                {/* RIGHT COLUMN */}
                <div className="space-y-6">
                    {/* 3) Candidates */}
                    <CardBox
                        icon={<CodeIcon className="h-5 w-5" />}
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
                        <div className="max-h-[60vh] overflow-y-auto pr-1">
                            <div className="flex flex-col gap-3">
                                {sortedCandidates.length === 0 ? (
                                    <div className="text-sm text-slate-500 italic px-1">
                                        No candidates yet — start a stream to see generated code.
                                    </div>
                                ) : null}

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
                                            onKeyDown={(e) => { if (e.key === "Enter" || e.key === " ") setSelectedId(c.id); }}
                                            className={`rounded-2xl border p-3 bg-white cursor-pointer w-full ${selectedStyle}`}
                                        >
                                            <div className="flex items-start justify-between">
                                                <div>
                                                    <div className="font-semibold leading-tight">{c.name}</div>
                                                    <div className="text-xs text-slate-500 mt-0.5">{c.origin === "archcode" ? "ARCHCODE" : "Existing"}</div>
                                                </div>
                                                <div className="text-right text-xs">
                                                    <div>Score: <span className="font-semibold">{d.score}</span></div>
                                                    <div>Tests: <span
                                                        className="font-semibold">{d.pass}/{d.total}</span></div>
                                                    <div className={d.ok ? "text-emerald-600" : "text-amber-600"}>{d.ok ? "FR meets" : "FR may violate"}</div>
                                                </div>
                                            </div>

                                            {/*<div className="mt-2 flex flex-wrap gap-1">*/}
                                            {/*    {tagBadges.map((t, i) => (*/}
                                            {/*        <Badge key={i} className="bg-slate-50 border-slate-200">*/}
                                            {/*            {t}*/}
                                            {/*        </Badge>*/}
                                            {/*    ))}*/}
                                            {/*</div>*/}
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    </CardBox>

                    {/* 4) Selected Code */}
                    <CardBox icon={<CheckCircle2 className="h-5 w-5" />} title="4) Selected Code">
                        {!selected ? (
                            <div className="text-slate-500 text-sm">No selection. Stream and pick a candidate.</div>
                        ) : (
                            <div className="space-y-3">
                                <div className="flex items-center justify-between">
                                    <div>
                                        <div className="text-xs uppercase tracking-wider text-slate-500">Chosen Candidate</div>
                                        <div className="font-semibold text-lg">{selected.name}</div>
                                    </div>
                                    <CopyButton text={selectedCode} />
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
                                            minimap: { enabled: false },
                                            scrollBeyondLastLine: false,
                                            wordWrap: "on",
                                            padding: { top: 12, bottom: 12 },
                                            automaticLayout: true,
                                        }}
                                    />
                                </div>
                                {/*<div className="grid grid-cols-2 gap-2">*/}
                                {/*    <div className="rounded-xl border p-3"><div className="text-xs text-slate-500">Complexity</div><div className="font-medium">{selected.metrics.timeComplexityLabel}</div></div>*/}
                                {/*    <div className="rounded-xl border p-3"><div className="text-xs text-slate-500">Cyclomatic</div><div className="font-medium">{selected.metrics.cyclomaticComplexity}</div></div>*/}
                                {/*    <div className="rounded-xl border p-3"><div className="text-xs text-slate-500">Robust</div><div className="font-medium">{selected.metrics.robustInputChecks ? "Yes" : "No"}</div></div>*/}
                                {/*    <div className="rounded-xl border p-3"><div className="text-xs text-slate-500">Edge-safe</div><div className="font-medium">{selected.metrics.handlesNegativesAndZero ? "Yes" : "No"}</div></div>*/}
                                {/*</div>*/}
                                {/*<div className="inline-flex items-center gap-2 text-amber-700 bg-amber-50 border border-amber-200 rounded-full px-3 py-1 text-sm">*/}
                                {/*    Manually selected*/}
                                {/*</div>*/}
                            </div>
                        )}
                    </CardBox>
                </div>
            </div>
        </div>
    );
}
