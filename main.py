import streamlit as st
import hashlib
import html
import re


# =========================================================
# PAGE
# =========================================================

st.set_page_config(
    page_title="THE DEBUT ARCHIVE",
    page_icon="⚡",
    layout="centered"
)


# =========================================================
# CRAZY BACKGROUND CSS
# =========================================================

st.markdown(
    """
<style>

/* =======================================================
   전체 화면
   ======================================================= */

.stApp {
    min-height: 100vh;

    background:
        radial-gradient(
            circle at 15% 20%,
            rgba(255, 0, 140, 0.28),
            transparent 25%
        ),
        radial-gradient(
            circle at 85% 15%,
            rgba(90, 0, 255, 0.30),
            transparent 25%
        ),
        radial-gradient(
            circle at 50% 90%,
            rgba(0, 180, 255, 0.20),
            transparent 28%
        ),
        linear-gradient(
            120deg,
            #020205,
            #0b0313,
            #02020a,
            #12000e,
            #020205
        );

    background-size:
        180% 180%,
        200% 200%,
        170% 170%,
        400% 400%;

    animation:
        backgroundChaos 7s ease-in-out infinite alternate;

    color: #ffffff;

    overflow-x: hidden;
}


/* =======================================================
   배경 움직임
   ======================================================= */

@keyframes backgroundChaos {

    0% {
        background-position:
            0% 0%,
            100% 0%,
            50% 100%,
            0% 50%;
    }

    25% {
        background-position:
            100% 20%,
            0% 80%,
            80% 0%,
            100% 0%;
    }

    50% {
        background-position:
            20% 100%,
            80% 10%,
            0% 50%,
            50% 100%;
    }

    75% {
        background-position:
            90% 60%,
            10% 20%,
            100% 80%,
            0% 0%;
    }

    100% {
        background-position:
            0% 0%,
            100% 100%,
            30% 0%,
            100% 100%;
    }
}


/* =======================================================
   화면 전체 번쩍이는 오버레이
   ======================================================= */

.stApp::before {

    content: "";

    position: fixed;

    inset: 0;

    pointer-events: none;

    z-index: 0;

    background:
        linear-gradient(
            115deg,
            transparent 0%,
            rgba(255, 0, 140, 0.08) 25%,
            transparent 40%,
            rgba(80, 0, 255, 0.08) 65%,
            transparent 80%
        );

    background-size: 250% 250%;

    animation:
        lightSweep 3.5s linear infinite;

    mix-blend-mode: screen;
}


@keyframes lightSweep {

    0% {
        background-position: -150% 0%;
    }

    100% {
        background-position: 150% 100%;
    }
}


/* =======================================================
   미친 네온 플래시
   ======================================================= */

.stApp::after {

    content: "";

    position: fixed;

    inset: 0;

    pointer-events: none;

    z-index: 1;

    background:
        radial-gradient(
            circle at 30% 30%,
            rgba(255, 0, 100, 0.12),
            transparent 18%
        ),
        radial-gradient(
            circle at 70% 70%,
            rgba(0, 200, 255, 0.10),
            transparent 20%
        );

    animation:
        crazyPulse 1.8s infinite;

    mix-blend-mode: screen;
}


@keyframes crazyPulse {

    0%,
    100% {
        opacity: 0.25;
        filter: blur(0px);
    }

    45% {
        opacity: 0.8;
        filter: blur(5px);
    }

    50% {
        opacity: 0.25;
    }

    52% {
        opacity: 0.9;
        filter: blur(10px);
    }

    55% {
        opacity: 0.25;
    }
}


/* =======================================================
   CONTENT
   ======================================================= */

.block-container {

    position: relative;

    z-index: 5;

    max-width: 850px;

    padding-top: 55px;
    padding-bottom: 100px;
}


/* =======================================================
   상단 작은 글씨
   ======================================================= */

.archive-label {

    text-align: center;

    color: #ff4db8;

    font-size: 11px;

    letter-spacing: 6px;

    font-weight: 900;

    margin-bottom: 22px;

    text-shadow:
        0 0 5px #ff008c,
        0 0 15px #ff008c,
        0 0 30px #8c00ff;

    animation:
        labelFlash 1.5s infinite alternate;
}


@keyframes labelFlash {

    from {
        opacity: 0.5;
    }

    to {
        opacity: 1;
    }
}


/* =======================================================
   메인 타이틀
   ======================================================= */

.main-title {

    text-align: center;

    font-size: 58px;

    line-height: 0.95;

    font-weight: 1000;

    letter-spacing: -3px;

    color: #ffffff;

    text-shadow:
        0 0 5px #ffffff,
        0 0 15px #ff00aa,
        0 0 35px #ff00aa,
        0 0 70px #7300ff;

    animation:
        titleChaos 2.2s infinite;

}


.main-title span {

    color: #ff55c8;

    text-shadow:
        0 0 5px #ff55c8,
        0 0 15px #ff00aa,
        0 0 35px #ff00aa,
        0 0 70px #7700ff;

}


@keyframes titleChaos {

    0%,
    100% {
        transform: translate(0, 0);
        filter: brightness(1);
    }

    45% {
        transform: translate(-1px, 1px);
        filter: brightness(1.2);
    }

    48% {
        transform: translate(2px, -1px);
        filter: brightness(2);
    }

    50% {
        transform: translate(-2px, 1px);
        filter: brightness(1);
    }

    52% {
        transform: translate(1px, -2px);
        filter: brightness(1.8);
    }
}


/* =======================================================
   부제
   ======================================================= */

.main-subtitle {

    text-align: center;

    color: #c2b5cc;

    font-size: 14px;

    line-height: 1.8;

    margin-top: 20px;

    margin-bottom: 45px;

    text-shadow:
        0 0 10px rgba(255, 0, 150, 0.4);
}


/* =======================================================
   입력 카드
   ======================================================= */

.input-panel {

    position: relative;

    background:
        linear-gradient(
            135deg,
            rgba(35, 10, 40, 0.92),
            rgba(5, 5, 14, 0.94)
        );

    border: 1px solid #ff20ad;

    padding: 30px;

    border-radius: 8px;

    box-shadow:
        0 0 10px rgba(255, 0, 150, 0.5),
        0 0 35px rgba(255, 0, 150, 0.25),
        inset 0 0 30px rgba(140, 0, 255, 0.08);

    animation:
        cardGlow 2s infinite alternate;

    margin-bottom: 20px;
}


@keyframes cardGlow {

    from {
        box-shadow:
            0 0 8px rgba(255,0,150,0.35),
            0 0 20px rgba(140,0,255,0.15);
    }

    to {
        box-shadow:
            0 0 18px rgba(255,0,150,0.8),
            0 0 55px rgba(140,0,255,0.35);
    }
}


.input-label {

    color: #ff75ce;

    font-size: 12px;

    letter-spacing: 3px;

    font-weight: 900;
}


.input-description {

    color: #8f8295;

    font-size: 12px;

    margin-top: 8px;
}


/* =======================================================
   STREAMLIT INPUT
   ======================================================= */

div[data-baseweb="input"] {

    background:
        rgba(5, 4, 10, 0.95) !important;

    border: 1px solid #59245b !important;

    border-radius: 5px !important;

    box-shadow:
        0 0 12px rgba(255, 0, 150, 0.15);

}


div[data-baseweb="input"]:focus-within {

    border-color: #ff35bb !important;

    box-shadow:
        0 0 8px #ff00aa,
        0 0 25px rgba(255,0,170,0.45) !important;

}


div[data-baseweb="input"] input {

    color: #ffffff !important;

    caret-color: #ff42bf !important;

}


/* =======================================================
   BUTTON
   ======================================================= */

div.stButton > button {

    width: 100%;

    border: 1px solid #ff54c7;

    border-radius: 5px;

    background:
        linear-gradient(
            90deg,
            #6e0068,
            #ff008c,
            #6500ff
        );

    background-size: 250% 100%;

    color: white;

    font-size: 14px;

    font-weight: 900;

    letter-spacing: 2px;

    padding: 15px;

    box-shadow:
        0 0 10px #ff008c,
        0 0 30px rgba(255,0,140,0.35);

    animation:
        buttonMove 2s linear infinite;

}


@keyframes buttonMove {

    0% {
        background-position: 0% 50%;
    }

    100% {
        background-position: 250% 50%;
    }
}


div.stButton > button:hover {

    transform: scale(1.02);

    box-shadow:
        0 0 15px #ff00aa,
        0 0 50px #7700ff;

}


/* =======================================================
   RESULT
   ======================================================= */

.result-container {

    margin-top: 35px;

    padding: 38px 30px;

    border-radius: 8px;

    background:
        linear-gradient(
            145deg,
            rgba(25, 10, 30, 0.97),
            rgba(4, 4, 10, 0.97)
        );

    border: 1px solid #9b37ff;

    box-shadow:
        0 0 12px rgba(255,0,150,0.45),
        0 0 40px rgba(120,0,255,0.25),
        inset 0 0 50px rgba(255,0,150,0.03);

}


/* =======================================================
   REPORT
   ======================================================= */

.report-label {

    text-align: center;

    color: #ff46bc;

    font-size: 10px;

    letter-spacing: 5px;

    font-weight: 900;

}


.report-name {

    text-align: center;

    color: #d8ccd9;

    font-size: 18px;

    letter-spacing: 4px;

    margin-top: 12px;
}


.report-line {

    height: 1px;

    margin: 30px 0;

    background:
        linear-gradient(
            90deg,
            transparent,
            #ff00aa,
            #8c00ff,
            transparent
        );

    box-shadow:
        0 0 10px #ff00aa;
}


/* =======================================================
   STAGE NAME
   ======================================================= */

.stage-label {

    text-align: center;

    color: #8f8195;

    font-size: 11px;

    letter-spacing: 4px;
}


.stage-name {

    text-align: center;

    font-size: 70px;

    font-weight: 1000;

    letter-spacing: -4px;

    color: #ffffff;

    margin-top: 8px;

    text-shadow:
        0 0 5px white,
        0 0 15px #ff00aa,
        0 0 35px #ff00aa,
        0 0 65px #7700ff;

    animation:
        stagePulse 1.7s infinite alternate;
}


@keyframes stagePulse {

    from {
        filter: brightness(0.9);
    }

    to {
        filter: brightness(1.5);
    }
}


.stage-pronunciation {

    text-align: center;

    color: #9f8da6;

    font-size: 12px;

    letter-spacing: 3px;
}


/* =======================================================
   POSITION
   ======================================================= */

.position-box {

    margin-top: 30px;

    padding: 25px;

    text-align: center;

    background:
        linear-gradient(
            120deg,
            rgba(255,0,150,0.10),
            rgba(100,0,255,0.10)
        );

    border: 1px solid #5e3b78;

    box-shadow:
        0 0 25px rgba(120,0,255,0.15);
}


.position-label {

    color: #93859c;

    font-size: 10px;

    letter-spacing: 4px;
}


.position-name {

    color: #ffffff;

    font-size: 29px;

    font-weight: 900;

    margin-top: 8px;

    text-shadow:
        0 0 10px rgba(255,0,170,0.5);
}


/* =======================================================
   EVIDENCE
   ======================================================= */

.evidence-title {

    color: #f0eaf2;

    font-size: 17px;

    font-weight: 900;

    margin-top: 38px;

    margin-bottom: 18px;

}


.evidence-item {

    padding: 16px;

    margin-bottom: 10px;

    background:
        linear-gradient(
            90deg,
            rgba(255,0,150,0.07),
            rgba(100,0,255,0.03)
        );

    border-left: 3px solid #ff18ae;

    box-shadow:
        0 0 12px rgba(255,0,150,0.06);
}


.evidence-number {

    color: #ff45c0;

    font-size: 10px;

    letter-spacing: 3px;

    font-weight: 900;
}


.evidence-text {

    color: #aaa0ad;

    font-size: 13px;

    line-height: 1.9;

    margin-top: 5px;
}


/* =======================================================
   ANALYSIS
   ======================================================= */

.analysis-title {

    color: #f0eaf2;

    font-size: 17px;

    font-weight: 900;

    margin-top: 38px;

    margin-bottom: 15px;
}


.metric-row {

    display: flex;

    justify-content: space-between;

    padding: 11px 0;

    border-bottom: 1px solid #27202b;

    color: #817681;

    font-size: 12px;
}


.metric-value {

    color: #ff76ce;

    font-weight: 900;

    text-shadow:
        0 0 8px rgba(255,0,150,0.5);
}


/* =======================================================
   CONCEPT
   ======================================================= */

.concept-box {

    margin-top: 30px;

    padding: 22px;

    border: 1px solid #422d52;

    background:
        rgba(15, 7, 20, 0.9);

}


.concept-label {

    color: #ff50bf;

    font-size: 10px;

    letter-spacing: 4px;

}


.concept-name {

    color: #eee9f1;

    font-size: 20px;

    font-weight: 900;

    margin-top: 7px;
}


.concept-description {

    color: #817681;

    font-size: 12px;

    line-height: 1.9;

    margin-top: 7px;
}


/* =======================================================
   DISCLAIMER
   ======================================================= */

.disclaimer {

    text-align: center;

    color: #625766;

    font-size: 10px;

    line-height: 1.9;

    margin-top: 35px;
}


/* =======================================================
   FOOTER
   ======================================================= */

.footer {

    text-align: center;

    color: #4f4055;

    font-size: 10px;

    letter-spacing: 3px;

    margin-top: 60px;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# DATA
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
# NAME ANALYSIS
# =========================================================

def analyze_name(name):

    korean = re.findall(r"[가-힣]", name)

    letters = re.findall(r"[A-Za-z가-힣]", name)

    length = len(letters)

    if length == 0:
        length = 1

    initials = []

    initial_list = [
        "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ",
        "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ",
        "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ",
        "ㅋ", "ㅌ", "ㅍ", "ㅎ"
    ]

    for char in korean:

        code = ord(char) - 0xAC00

        if 0 <= code <= 11171:

            initial_index = code // 588

            initials.append(
                initial_list[initial_index]
            )


    final_count = 0

    for char in korean:

        code = ord(char) - 0xAC00

        if 0 <= code <= 11171:

            if code % 28 != 0:
                final_count += 1


    vowel_list = [
        "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ",
        "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
        "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ",
        "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ",
        "ㅣ"
    ]


    vowel_score_map = {

        "ㅏ": 1,
        "ㅐ": 1,
        "ㅑ": 2,
        "ㅒ": 2,

        "ㅓ": -1,
        "ㅔ": -1,
        "ㅕ": -2,
        "ㅖ": -2,

        "ㅗ": 2,
        "ㅘ": 2,
        "ㅙ": 2,
        "ㅚ": 1,

        "ㅛ": 2,

        "ㅜ": -2,
        "ㅝ": -2,
        "ㅞ": -2,
        "ㅟ": -1,

        "ㅠ": -1,

        "ㅡ": 0,
        "ㅢ": 0,

        "ㅣ": 1
    }


    vowel_score = 0

    for char in korean:

        code = ord(char) - 0xAC00

        if 0 <= code <= 11171:

            vowel_index = (code % 588) // 28

            if vowel_index < len(vowel_list):

                vowel = vowel_list[vowel_index]

                vowel_score += vowel_score_map.get(
                    vowel,
                    0
                )


    return {
        "length": length,
        "korean_count": len(korean),
        "initials": initials,
        "final_count": final_count,
        "vowel_score": vowel_score
    }


# =========================================================
# RESULT ENGINE
# =========================================================

def make_result(name):

    data = analyze_name(name)

    seed = int(
        hashlib.sha256(
            name.encode("utf-8")
        ).hexdigest(),
        16
    )


    stage_index = seed % len(stage_names)

    position_index = (
        seed // 17
    ) % len(positions)

    concept_index = (
        seed // 31
    ) % len(concepts)


    stage = stage_names[stage_index]

    position = positions[position_index]

    concept = concepts[concept_index]


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


    evidence = []


    evidence.append(
        f"입력된 이름은 총 {data['length']}개의 문자 단위로 "
        f"분석되었습니다. 이 길이는 무대에서 빠르게 발음했을 때 "
        f"이름이 뭉개지지 않는 구조로 분류했습니다."
    )


    if data["initials"]:

        initial_text = " · ".join(
            data["initials"]
        )

        evidence.append(
            f"초성 구조는 [{initial_text}]로 분석됩니다. "
            f"초성의 변화 폭이 있는 이름은 발음에 리듬이 생기기 때문에 "
            f"무대에서 이름 자체가 하나의 퍼포먼스 요소로 작동할 가능성이 "
            f"높다고 판단했습니다."
        )

    else:

        evidence.append(
            "한글 초성이 없는 이름으로 분석되어 "
            "철자의 시각적 형태와 발음의 길이를 더 강하게 반영했습니다."
        )


    if data["final_count"] >= 2:

        evidence.append(
            f"총 {data['final_count']}개의 종성 구조가 확인되었습니다. "
            "종성이 많은 이름은 발음의 끝부분에 힘이 생기는 구조로 보고 "
            "강한 존재감을 요구하는 포지션과 연결했습니다."
        )

    else:

        evidence.append(
            "종성 구조가 비교적 가볍습니다. "
            "끝소리가 빠르게 정리되는 이름은 후렴구에서 이름을 "
            "반복했을 때 선명하게 들리는 구조로 해석했습니다."
        )


    if data["vowel_score"] > 1:

        evidence.append(
            "모음 분석에서 밝은 방향의 값이 상대적으로 높게 "
            "나타났습니다. 따라서 고음이나 선명한 포인트를 담당하는 "
            "역할과 연결하는 방향으로 분석했습니다."
        )

    elif data["vowel_score"] < -1:

        evidence.append(
            "모음 분석에서 무게감 있는 방향의 값이 상대적으로 "
            "높게 나타났습니다. 따라서 저음과 강한 표현력을 요구하는 "
            "포지션을 우선적으로 고려했습니다."
        )

    else:

        evidence.append(
            "모음의 밝고 어두운 방향성이 비교적 균형을 이루고 있습니다. "
            "이러한 균형형 구조는 특정 파트에만 의존하지 않는 "
            "올라운드형 무대 역할과 연결하기 적합하다고 판단했습니다."
        )


    evidence.append(
        f"최종 예명 '{stage}'는 원래 이름을 단순히 줄인 것이 아니라 "
        "무대에서 빠르게 인식할 수 있는 철자 수, 시각적인 균형, "
        "발음의 짧은 호흡을 기준으로 결정되었습니다."
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
    '<div class="archive-label">⚡ CLASSIFIED ENTERTAINMENT SYSTEM ⚡</div>',
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

이름의 구조 · 발음 · 리듬 · 음절 패턴을 기반으로<br>

가장 적합한 <b>예명과 포지션</b>을 산출합니다.

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# INPUT PANEL
# =========================================================

st.markdown(
    """
<div class="input-panel">

<div class="input-label">
CANDIDATE / NAME
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

if st.button("⚡ BEGIN THE DEBUT ANALYSIS ⚡"):

    if not name.strip():

        st.warning(
            "⚠️ 분석할 이름을 입력하십시오."
        )

    else:

        result = make_result(
            name.strip()
        )


        safe_name = html.escape(
            name.strip()
        )


        stage = result["stage"]

        pron = result["pronunciation"]

        position = result["position"]

        concept_name = result["concept"][0]

        concept_description = result["concept"][1]

        data = result["data"]


        # =================================================
        # RESULT HEADER
        # =================================================

        st.markdown(
            f"""
<div class="result-container">

<div class="report-label">
⚡ OFFICIAL DEBUT ANALYSIS ⚡
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
/ {pron} /
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

</div>
""",
            unsafe_allow_html=True
        )


        # =================================================
        # EVIDENCE
        # =================================================

        for i, item in enumerate(
            result["evidence"],
            start=1
        ):

            st.markdown(
                f"""
<div class="evidence-item">

<div class="evidence-number">
EVIDENCE {i:02d}
</div>

<div class="evidence-text">
{html.escape(item)}
</div>

</div>
""",
                unsafe_allow_html=True
            )


        # =================================================
        # ANALYSIS
        # =================================================

        st.markdown(
            """
<div class="analysis-title">
⚡ NAME STRUCTURE ANALYSIS
</div>
""",
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
<div class="metric-row">

<span>문자 수</span>

<span class="metric-value">
{data["length"]}
</span>

</div>

<div class="metric-row">

<span>한글 음절 수</span>

<span class="metric-value">
{data["korean_count"]}
</span>

</div>

<div class="metric-row">

<span>종성 포함 음절</span>

<span class="metric-value">
{data["final_count"]}
</span>

</div>

<div class="metric-row">

<span>모음 방향 지수</span>

<span class="metric-value">
{data["vowel_score"]}
</span>

</div>
""",
            unsafe_allow_html=True
        )


        # =================================================
        # CONCEPT
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
        # DISCLAIMER
        # =================================================

        st.markdown(
            """
<div class="disclaimer">

※ 본 결과는 이름의 문자 구조와 발음 등을 이용한
엔터테인먼트용 알고리즘입니다.<br>

실제 연예기획사의 캐스팅 또는 오디션 결과를 의미하지 않습니다.

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

⚡ THE DEBUT ARCHIVE · SYSTEM ONLINE ⚡

</div>
""",
    unsafe_allow_html=True
)
