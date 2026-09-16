import streamlit as st
import hashlib
import html
import re


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="THE DEBUT ARCHIVE",
    page_icon="✦",
    layout="centered"
)


# =========================================================
# 디자인
# =========================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 50% -10%,
            #25252a 0%,
            #101014 32%,
            #08080b 68%,
            #050506 100%
        );
    color: #eeeeee;
}

.block-container {
    max-width: 820px;
    padding-top: 55px;
    padding-bottom: 80px;
}


/* ---------- 상단 ---------- */

.archive-label {
    text-align: center;
    color: #77777f;
    font-size: 11px;
    letter-spacing: 5px;
    font-weight: 600;
    margin-bottom: 22px;
}

.main-title {
    text-align: center;
    color: #f2f2f4;
    font-size: 52px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.05;
    margin-bottom: 15px;
}

.main-title span {
    color: #b9a7ff;
}

.main-subtitle {
    text-align: center;
    color: #7e7e87;
    font-size: 14px;
    letter-spacing: 1px;
    line-height: 1.8;
    margin-bottom: 45px;
}


/* ---------- 입력 영역 ---------- */

.input-panel {
    background: linear-gradient(
        145deg,
        rgba(31, 31, 37, 0.95),
        rgba(14, 14, 18, 0.95)
    );

    border: 1px solid #303038;
    padding: 30px;
    border-radius: 4px;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.03);

    margin-bottom: 25px;
}

.input-label {
    color: #aaaab3;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 600;
    margin-bottom: 10px;
}

.input-description {
    color: #66666f;
    font-size: 12px;
    margin-bottom: 18px;
}


/* ---------- 버튼 ---------- */

div.stButton > button {
    width: 100%;

    background:
        linear-gradient(
            90deg,
            #8c79e8,
            #b09cff
        );

    color: #ffffff;

    border: none;
    border-radius: 3px;

    font-size: 14px;
    font-weight: 800;

    letter-spacing: 1px;

    padding: 14px;

    box-shadow:
        0 8px 25px rgba(130,110,230,0.22);

    transition: 0.25s;
}

div.stButton > button:hover {
    background:
        linear-gradient(
            90deg,
            #a291ff,
            #c0b1ff
        );

    box-shadow:
        0 10px 35px rgba(150,130,255,0.35);
}


/* ---------- 결과 ---------- */

.result-container {
    margin-top: 35px;

    background:
        linear-gradient(
            145deg,
            #19191f,
            #0d0d11
        );

    border: 1px solid #34343d;

    padding: 35px 30px;

    border-radius: 4px;

    box-shadow:
        0 25px 70px rgba(0,0,0,0.45);
}

.report-label {
    color: #777780;
    font-size: 10px;
    letter-spacing: 4px;
    text-align: center;
    margin-bottom: 15px;
}

.report-name {
    color: #eeeeef;
    font-size: 17px;
    text-align: center;
    letter-spacing: 3px;
}

.report-line {
    height: 1px;
    background:
        linear-gradient(
            90deg,
            transparent,
            #3d3d46,
            transparent
        );

    margin: 28px 0;
}


/* ---------- 예명 ---------- */

.stage-label {
    color: #74747d;
    text-align: center;
    font-size: 11px;
    letter-spacing: 3px;
    margin-bottom: 10px;
}

.stage-name {
    text-align: center;

    color: #c5b8ff;

    font-size: 64px;
    font-weight: 900;

    letter-spacing: -3px;

    text-shadow:
        0 0 25px rgba(170,150,255,0.22);

    margin-bottom: 8px;
}

.stage-pronunciation {
    text-align: center;
    color: #6e6e78;
    font-size: 11px;
    letter-spacing: 2px;
}


/* ---------- 포지션 ---------- */

.position-box {
    background:
        linear-gradient(
            135deg,
            rgba(145,125,235,0.10),
            rgba(255,255,255,0.015)
        );

    border: 1px solid #353344;

    padding: 25px;

    margin-top: 30px;

    text-align: center;
}

.position-label {
    color: #777482;
    font-size: 10px;
    letter-spacing: 3px;
    margin-bottom: 8px;
}

.position-name {
    color: #f0eff5;
    font-size: 27px;
    font-weight: 800;
}


/* ---------- 근거 ---------- */

.evidence-title {
    color: #e5e4e9;
    font-size: 16px;
    font-weight: 800;

    margin-top: 35px;
    margin-bottom: 20px;
}

.evidence-item {
    border-left: 2px solid #7161b8;

    padding: 14px 17px;

    background: rgba(255,255,255,0.025);

    margin-bottom: 10px;
}

.evidence-number {
    color: #8271cf;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 800;
}

.evidence-text {
    color: #a8a8b0;
    font-size: 13px;
    line-height: 1.8;
    margin-top: 5px;
}


/* ---------- 콘셉트 ---------- */

.concept-box {
    margin-top: 30px;

    padding: 22px;

    border: 1px solid #2e2e36;

    background: #111116;
}

.concept-label {
    color: #777780;
    font-size: 10px;
    letter-spacing: 3px;
    margin-bottom: 10px;
}

.concept-name {
    color: #d5d0ed;
    font-size: 19px;
    font-weight: 700;
}

.concept-description {
    color: #797982;
    font-size: 12px;
    line-height: 1.8;
    margin-top: 8px;
}


/* ---------- 점수 ---------- */

.analysis-title {
    color: #e4e3e8;
    font-size: 16px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 18px;
}

.metric-row {
    display: flex;
    justify-content: space-between;

    color: #85858e;

    font-size: 12px;

    padding: 10px 0;

    border-bottom: 1px solid #222229;
}

.metric-value {
    color: #bdb5e9;
    font-weight: 700;
}


/* ---------- 하단 ---------- */

.disclaimer {
    text-align: center;

    color: #55555d;

    font-size: 10px;

    line-height: 1.8;

    margin-top: 35px;
}

.footer {
    text-align: center;

    color: #3f3f47;

    font-size: 10px;

    letter-spacing: 2px;

    margin-top: 55px;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# 데이터
# =========================================================

stage_names = [
    "LUNE",
    "NOIR",
    "RIN",
    "VEIL",
    "NOVA",
    "ELLE",
    "ROAN",
    "VANE",
    "LIO",
    "MUSE",
    "RAY",
    "NIX",
    "ARIA",
    "SENA",
    "IVY",
    "REI"
]


positions = [
    "메인보컬",
    "리드보컬",
    "메인댄서",
    "리드댄서",
    "메인래퍼",
    "리드래퍼",
    "센터",
    "비주얼",
    "올라운더",
    "퍼포먼스 리더"
]


concepts = [
    (
        "DARK ELEGANCE",
        "차가운 조명과 절제된 움직임을 중심으로 하는 고급스러운 다크 콘셉트."
    ),
    (
        "MIDNIGHT POP",
        "새벽의 도시와 네온사인을 연상시키는 세련된 신스팝 콘셉트."
    ),
    (
        "PURE ICON",
        "불필요한 장식을 최소화하고 멤버의 존재감 자체를 강조하는 콘셉트."
    ),
    (
        "VELVET NOIR",
        "부드러운 이미지와 강렬한 카리스마를 동시에 보여주는 콘셉트."
    ),
    (
        "FUTURE ROMANCE",
        "미래적인 사운드와 감성적인 비주얼을 결합한 콘셉트."
    ),
    (
        "SILVER MOON",
        "차가운 은빛 색감과 몽환적인 분위기를 강조하는 콘셉트."
    )
]


# =========================================================
# 한글 이름 분석
# =========================================================

def analyze_name(name):

    # 한글만 추출
    korean = re.findall(r"[가-힣]", name)

    # 영문 등도 고려
    letters = re.findall(r"[A-Za-z가-힣]", name)

    length = len(letters)

    if length == 0:
        length = 1

    # 초성
    initials = []

    for char in korean:
        code = ord(char) - 0xAC00

        if 0 <= code <= 11171:
            initial_index = code // 588

            initial_list = [
                "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ",
                "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ",
                "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ",
                "ㅋ", "ㅌ", "ㅍ", "ㅎ"
            ]

            initials.append(initial_list[initial_index])

    # 종성 여부
    final_count = 0

    for char in korean:
        code = ord(char) - 0xAC00

        if 0 <= code <= 11171:
            if code % 28 != 0:
                final_count += 1

    # 모음 성격
    vowel_score = 0

    vowel_patterns = {
        "ㅏ": 1,
        "ㅑ": 2,
        "ㅓ": -1,
        "ㅕ": -2,
        "ㅗ": 2,
        "ㅛ": 2,
        "ㅜ": -2,
        "ㅠ": -1,
        "ㅡ": 0,
        "ㅣ": 1
    }

    for char in korean:
        # 아주 단순한 음절 코드 기반 분석
        code = ord(char) - 0xAC00

        if 0 <= code <= 11171:

            vowel_index = (code % 588) // 28

            vowel_list = [
                "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ",
                "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
                "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ",
                "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ",
                "ㅣ"
            ]

            if vowel_index < len(vowel_list):
                vowel = vowel_list[vowel_index]
                vowel_score += vowel_patterns.get(vowel, 0)

    return {
        "length": length,
        "korean_count": len(korean),
        "initials": initials,
        "final_count": final_count,
        "vowel_score": vowel_score
    }


# =========================================================
# 이름 → 결과 결정
# =========================================================

def make_result(name):

    data = analyze_name(name)

    seed = int(
        hashlib.sha256(
            name.encode("utf-8")
        ).hexdigest(),
        16
    )

    # 결과가 이름에 따라 일정하게 나오도록
    index1 = seed % len(stage_names)

    index2 = (seed // 17) % len(positions)

    index3 = (seed // 31) % len(concepts)

    stage = stage_names[index1]

    position = positions[index2]

    concept = concepts[index3]

    # -----------------------------------------------------
    # 예명 발음
    # -----------------------------------------------------

    pronunciation = {
        "LUNE": "룬",
        "NOIR": "누아르",
        "RIN": "린",
        "VEIL": "베일",
        "NOVA": "노바",
        "ELLE": "엘",
        "ROAN": "로안",
        "VANE": "베인",
        "LIO": "리오",
        "MUSE": "뮤즈",
        "RAY": "레이",
        "NIX": "닉스",
        "ARIA": "아리아",
        "SENA": "세나",
        "IVY": "아이비",
        "REI": "레이"
    }

    pron = pronunciation[stage]

    # -----------------------------------------------------
    # 근거 생성
    # -----------------------------------------------------

    evidence = []

    # 근거 1
    evidence.append(
        f"입력된 이름은 총 {data['length']}개의 문자 단위로 분석되었습니다. "
        f"이 길이는 무대에서 빠르게 발음했을 때 이름이 뭉개지지 않는 "
        f"중단 길이 구조로 분류했습니다."
    )

    # 근거 2
    if data["initials"]:
        initial_text = " · ".join(data["initials"])

        evidence.append(
            f"초성 구조는 [{initial_text}]로 분석됩니다. "
            f"초성의 변화 폭이 있는 이름은 발음에 리듬이 생기기 때문에 "
            f"퍼포먼스 중심의 예명 설계에 적합하다고 판단했습니다."
        )
    else:
        evidence.append(
            "한글 초성이 없는 이름으로 분석되어 철자 자체의 시각적 인상을 "
            "예명 결정에 더 강하게 반영했습니다."
        )

    # 근거 3
    if data["final_count"] >= 2:
        evidence.append(
            f"총 {data['final_count']}개의 종성 구조가 확인되었습니다. "
            f"종성이 많은 이름은 발음의 끝부분에 힘이 생기는 경향이 있다고 보고, "
            f"무대에서 존재감이 강하게 느껴지는 포지션과 연결했습니다."
        )
    else:
        evidence.append(
            "종성 구조가 비교적 가벼운 편입니다. "
            "끝소리가 빠르게 정리되는 이름은 보컬이나 댄스 포지션에서 "
            "짧은 후렴구를 강조하기 좋은 이름 구조로 해석했습니다."
        )

    # 근거 4
    if data["vowel_score"] > 1:
        evidence.append(
            "모음 분석에서 밝은 방향의 점수가 상대적으로 높게 나타났습니다. "
            "이에 따라 밝은 고음이나 선명한 포인트를 담당하는 역할을 "
            "배정하는 방향으로 결과를 조정했습니다."
        )
    elif data["vowel_score"] < -1:
        evidence.append(
            "모음 분석에서 낮고 무게감 있는 방향의 점수가 상대적으로 높았습니다. "
            "따라서 저음과 강한 표정 연출이 가능한 포지션을 우선적으로 고려했습니다."
        )
    else:
        evidence.append(
            "모음의 밝고 어두운 방향성이 한쪽으로 치우치지 않았습니다. "
            "이런 균형형 구조는 특정 포지션에 한정하기보다 팀의 중심 역할을 "
            "수행하는 방향으로 해석했습니다."
        )

    # 근거 5
    evidence.append(
        f"최종 예명 '{stage}'는 원래 이름의 음절을 그대로 옮긴 것이 아니라, "
        f"무대에서 기억하기 쉬운 짧은 음절 구조와 시각적인 철자 형태를 기준으로 "
        f"선택되었습니다. 한국어 발음은 '{pron}'으로 설정했습니다."
    )

    return {
        "stage": stage,
        "pronunciation": pron,
        "position": position,
        "concept": concept,
        "evidence": evidence,
        "data": data
    }


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="archive-label">CONFIDENTIAL / ENTERTAINMENT DIVISION</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="main-title">
THE <span>DEBUT</span><br>
ARCHIVE
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="main-subtitle">
당신의 이름이 무대 위에서 어떻게 불려야 하는지 분석합니다.<br>
이름의 구조 · 발음 · 리듬 · 음절 패턴을 기반으로 예명과 포지션을 결정합니다.
</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# INPUT
# =========================================================

st.markdown(
    """
<div class="input-panel">

<div class="input-label">
CANDIDATE NAME
</div>

<div class="input-description">
데뷔할 사람의 이름을 입력하십시오.
</div>

</div>
""",
    unsafe_allow_html=True
)

name = st.text_input(
    "이름",
    placeholder="예: 김민지",
    label_visibility="collapsed",
    max_chars=30
)


# =========================================================
# BUTTON
# =========================================================

if st.button("✦ BEGIN THE ANALYSIS"):

    if not name.strip():

        st.warning("분석할 이름을 입력하십시오.")

    else:

        result = make_result(name.strip())

        safe_name = html.escape(name.strip())

        stage = result["stage"]
        pron = result["pronunciation"]
        position = result["position"]
        concept_name = result["concept"][0]
        concept_description = result["concept"][1]

        data = result["data"]


        # =================================================
        # RESULT
        # =================================================

        st.markdown(
            f"""
<div class="result-container">

<div class="report-label">
OFFICIAL DEBUT ANALYSIS
</div>

<div class="report-name">
{safe_name}
</div>

<div class="report-line"></div>

<div class="stage-label">
RECOMMENDED STAGE NAME
</div>

<div class="stage-name">
{stage}
</div>

<div class="stage-pronunciation">
/{pron}/
</div>

<div class="position-box">

<div class="position-label">
PRIMARY POSITION
</div>

<div class="position-name">
{position}
</div>

</div>

<div class="evidence-title">
WHY THIS RESULT?
</div>
""",
            unsafe_allow_html=True
        )


        # =================================================
        # 근거 출력
        # =================================================

        for i, item in enumerate(
            result["evidence"],
            start=1
        ):

            safe_item = html.escape(item)

            st.markdown(
                f"""
<div class="evidence-item">

<div class="evidence-number">
EVIDENCE {i:02d}
</div>

<div class="evidence-text">
{safe_item}
</div>

</div>
""",
                unsafe_allow_html=True
            )


        # =================================================
        # 분석 수치
        # =================================================

        st.markdown(
            """
<div class="analysis-title">
NAME STRUCTURE ANALYSIS
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
<div class="metric-row">
    <span>문자 수</span>
    <span class="metric-value">{data["length"]}</span>
</div>

<div class="metric-row">
    <span>한글 음절 수</span>
    <span class="metric-value">{data["korean_count"]}</span>
</div>

<div class="metric-row">
    <span>종성 포함 음절</span>
    <span class="metric-value">{data["final_count"]}</span>
</div>

<div class="metric-row">
    <span>모음 방향 지수</span>
    <span class="metric-value">{data["vowel_score"]}</span>
</div>
""",
            unsafe_allow_html=True
        )


        # =================================================
        # 콘셉트
        # =================================================

        st.markdown(
            f"""
<div class="concept-box">

<div class="concept-label">
DEBUT CONCEPT
</div>

<div class="concept-name">
{html.escape(concept_name)}
</div>

<div class="concept-description">
{html.escape(concept_description)}
</div>

</div>
""",
            unsafe_allow_html=True
        )


        # =================================================
        # 마지막
        # =================================================

        st.markdown(
            """
<div class="disclaimer">
※ 본 분석은 이름의 문자 구조와 발음 등을 이용한
엔터테인먼트용 알고리즘입니다.<br>
실제 연예기획사의 오디션이나 캐스팅 결과를 의미하지 않습니다.
</div>
""",
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
<div class="footer">
THE DEBUT ARCHIVE · INTERNAL ANALYSIS SYSTEM
</div>
""",
    unsafe_allow_html=True
)
