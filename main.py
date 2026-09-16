import streamlit as st
import random
import hashlib
import html

# ============================================
# 페이지 기본 설정
# ============================================

st.set_page_config(
    page_title="그 이름을 입력하지 마세요...",
    page_icon="👁️",
    layout="centered"
)

# ============================================
# 무서운 분위기 CSS
# ============================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(
            circle at 50% 15%,
            #351522 0%,
            #13090e 35%,
            #050306 75%,
            #000000 100%
        );
    color: #dddddd;
}

.block-container {
    max-width: 720px;
    padding-top: 45px;
    padding-bottom: 60px;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #d9a0ad;
    line-height: 1.35;
    text-shadow:
        0 0 8px #8f263f,
        0 0 20px #5a1025,
        0 0 40px #350b17;
    margin-bottom: 8px;
}

.sub-title {
    text-align: center;
    color: #765963;
    font-size: 14px;
    letter-spacing: 3px;
    margin-bottom: 35px;
}

.eye {
    text-align: center;
    font-size: 70px;
    margin-bottom: 5px;
    text-shadow:
        0 0 10px #9b2945,
        0 0 30px #6c1028;
}

.intro-card {
    background: rgba(18, 10, 15, 0.9);
    border: 1px solid #4c202d;
    border-radius: 8px;
    padding: 28px;
    margin-bottom: 25px;
    box-shadow:
        0 0 30px rgba(120, 20, 50, 0.15),
        inset 0 0 20px rgba(0, 0, 0, 0.5);
}

.intro-title {
    text-align: center;
    color: #c68a98;
    font-size: 20px;
    font-weight: bold;
}

.intro-text {
    text-align: center;
    color: #806873;
    line-height: 1.9;
    font-size: 15px;
}

.result-card {
    background:
        linear-gradient(
            145deg,
            rgba(34, 13, 22, 0.98),
            rgba(7, 6, 9, 0.98)
        );
    border: 1px solid #68263a;
    border-radius: 8px;
    padding: 32px 25px;
    margin-top: 25px;
    box-shadow:
        0 0 35px rgba(140, 20, 55, 0.25),
        inset 0 0 35px rgba(0, 0, 0, 0.7);
}

.result-name {
    text-align: center;
    color: #b87b89;
    font-size: 20px;
    letter-spacing: 2px;
}

.result-title {
    text-align: center;
    color: #e0a5b2;
    font-size: 30px;
    font-weight: bold;
    margin: 20px 0;
    text-shadow:
        0 0 10px #70223a,
        0 0 25px #3c0d1d;
}

.result-text {
    text-align: center;
    color: #c8b9bd;
    font-size: 16px;
    line-height: 2;
}

.warning-box {
    background: rgba(70, 10, 25, 0.22);
    border: 1px solid #51202f;
    border-radius: 6px;
    padding: 18px;
    margin-top: 20px;
}

.warning-title {
    text-align: center;
    color: #a93653;
    font-weight: bold;
    font-size: 15px;
}

.warning-text {
    text-align: center;
    color: #9b7a83;
    line-height: 1.8;
    font-size: 14px;
}

.symbol {
    text-align: center;
    font-size: 52px;
    margin: 15px 0;
    filter: drop-shadow(0 0 12px #77233a);
}

.number {
    text-align: center;
    color: #9b7781;
    font-size: 18px;
    letter-spacing: 8px;
}

.divider {
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        #652438,
        transparent
    );
    margin: 25px 0;
}

.footer {
    text-align: center;
    color: #3f3035;
    font-size: 11px;
    line-height: 2;
    margin-top: 50px;
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(
        135deg,
        #52172a,
        #801e3b
    );
    color: #f0dce1;
    border: 1px solid #96304c;
    border-radius: 5px;
    padding: 12px;
    font-size: 16px;
    font-weight: bold;
}

div.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #721d37,
        #a5294b
    );
    color: white;
    box-shadow:
        0 0 20px rgba(180, 35, 75, 0.4);
}

div[data-baseweb="input"] {
    background-color: #0e090c;
}

div[data-baseweb="input"] input {
    color: #ead9de !important;
}

</style>
""",
    unsafe_allow_html=True
)

# ============================================
# 신점(?) 데이터
# ============================================

fortunes = [
    {
        "title": "빈 의자",
        "message": (
            "당신의 이름에서는 이상하게도 '자리'라는 기운이 반복됩니다. "
            "누군가 떠난 자리에 새로운 무언가가 들어오는 흐름이 보입니다."
        ),
        "warning": (
            "오늘 밤 혼자 있는 방에서 빈 의자를 오래 바라보지 마세요."
        )
    },
    {
        "title": "새벽 3시의 그림자",
        "message": (
            "당신의 이름을 따라 어두운 그림자가 길게 드리워져 있습니다. "
            "최근 잊고 있던 기억 하나가 갑자기 떠오를 수 있습니다."
        ),
        "warning": (
            "새벽에 갑자기 잠에서 깨어났다면 바로 뒤를 돌아보지 마세요."
        )
    },
    {
        "title": "닫힌 문",
        "message": (
            "당신 앞에는 오래 닫혀 있던 문 하나가 보입니다. "
            "그 문은 아직 열리지 않았지만, 누군가 안쪽에서 기다리고 있는 듯합니다."
        ),
        "warning": (
            "밤에 집 안에서 문이 닫히는 소리가 들려도 급하게 확인하지 마세요."
        )
    },
    {
        "title": "붉은 달",
        "message": (
            "당신의 이름에는 붉은 달의 흔적이 남아 있습니다. "
            "가까운 시일 안에 과거와 관련된 사람이나 장소가 다시 눈앞에 나타날 수 있습니다."
        ),
        "warning": (
            "오래 연락하지 않았던 사람에게 먼저 연락하는 것은 잠시 미뤄보세요."
        )
    },
    {
        "title": "이름을 부르는 목소리",
        "message": (
            "당신의 이름에는 묘하게 강한 울림이 있습니다. "
            "예상하지 못했던 순간 누군가 당신의 이름을 부르는 일이 생길 수 있습니다."
        ),
        "warning": (
            "혼자 있을 때 들린 것 같은 목소리에 바로 대답하지 마세요."
        )
    },
    {
        "title": "검은 나비",
        "message": (
            "검은 나비 한 마리가 당신의 운세 주변을 맴돌고 있습니다. "
            "변화의 기운이 강해지고 있으며 예상하지 못했던 일이 찾아올 수 있습니다."
        ),
        "warning": (
            "평소와 다르게 이상하게 마음에 걸리는 장소는 오늘은 피하는 것도 좋습니다."
        )
    },
    {
        "title": "뒤에서 들리는 발소리",
        "message": (
            "당신의 이름 뒤쪽에서 아주 작은 발소리가 들립니다. "
            "당신이 멈추면 멈추고, 걸으면 다시 따라오는 기운입니다."
        ),
        "warning": (
            "밤길에서 발소리가 들린다고 바로 뒤를 확인하지 마세요."
        )
    },
    {
        "title": "거울 속의 시선",
        "message": (
            "오늘 당신의 운세에는 거울이라는 상징이 강하게 나타납니다. "
            "평소보다 자신의 모습이 낯설게 느껴지는 순간이 있을 수 있습니다."
        ),
        "warning": (
            "늦은 밤 거울을 오래 바라보는 행동은 오늘만큼은 피하세요."
        )
    },
    {
        "title": "오지 않은 전화",
        "message": (
            "당신의 이름 주변에 아직 울리지 않은 전화의 기운이 있습니다. "
            "기다리지 않았던 연락이 찾아올 가능성이 보입니다."
        ),
        "warning": (
            "모르는 번호에서 전화가 와도 너무 늦은 시간이라면 받지 마세요."
        )
    },
    {
        "title": "빈 방",
        "message": (
            "당신의 운세에는 아무도 없는 방이 반복해서 나타납니다. "
            "그 방에는 아무것도 없어야 하지만 이상하게 누군가 있었던 흔적이 남아 있습니다."
        ),
        "warning": (
            "오늘 밤 집 안에서 평소와 다른 작은 소리가 들려도 너무 걱정하지 마세요."
        )
    }
]

# ============================================
# 이름에 따라 결과 만들기
# ============================================

def get_fortune(name):
    # 이름을 숫자로 변환
    seed = int(
        hashlib.sha256(
            name.encode("utf-8")
        ).hexdigest(),
        16
    )

    random_generator = random.Random(seed)

    fortune = random_generator.choice(fortunes)

    symbols = [
        "🌙",
        "👁️",
        "🥀",
        "🪞",
        "🗝️",
        "🦋",
        "🐦‍⬛"
    ]

    symbol = random_generator.choice(symbols)

    numbers = [
        random_generator.randint(1, 9),
        random_generator.randint(1, 9),
        random_generator.randint(1, 9)
    ]

    return fortune, symbol, numbers


# ============================================
# 화면 시작
# ============================================

st.markdown(
    '<div class="eye">👁️</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="main-title">
    그 이름을<br>
    입력하지 마세요...
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="sub-title">
    당신의 이름에 남아 있는 흔적을 읽습니다
</div>
""",
    unsafe_allow_html=True
)

# ============================================
# 안내 카드
# ============================================

st.markdown(
    """
<div class="intro-card">

<div class="intro-title">
    👁️ 이름을 알고 있습니다.
</div>

<br>

<div class="intro-text">
    이름을 입력하면<br>
    당신에게 남아 있는 기운을 확인합니다.<br><br>
    <span style="color:#a33650;">
    단 한 글자라도 틀리지 마세요.
    </span>
</div>

</div>
""",
    unsafe_allow_html=True
)

# ============================================
# 이름 입력
# ============================================

name = st.text_input(
    "이름",
    placeholder="이름을 입력하세요...",
    label_visibility="collapsed"
)

st.write("")

# ============================================
# 확인 버튼
# ============================================

if st.button("👁️ 내 이름의 기운을 확인한다"):

    if not name.strip():

        st.warning("먼저 이름을 입력하세요.")

    else:

        clean_name = name.strip()

        fortune, symbol, numbers = get_fortune(clean_name)

        # HTML에 안전하게 이름 표시
        safe_name = html.escape(clean_name)

        # 결과 카드
        result_html = f"""
<div class="result-card">

<div class="result-name">
「 {safe_name} 」
</div>

<div class="divider"></div>

<div class="result-title">
{fortune["title"]}
</div>

<div class="result-text">
{fortune["message"]}
</div>

<div class="divider"></div>

<div style="
    text-align:center;
    color:#80656e;
    font-size:14px;
">
오늘 당신을 따라오는 상징
</div>

<div class="symbol">
{symbol}
</div>

<div class="number">
{" · ".join(map(str, numbers))}
</div>

<div class="warning-box">

<div class="warning-title">
⚠️ 주의
</div>

<br>

<div class="warning-text">
{fortune["warning"]}
</div>

</div>

</div>
"""

        st.markdown(
            result_html,
            unsafe_allow_html=True
        )

        # 아래 안내
        st.markdown(
            """
<div class="small-warning">

<br>

이 결과는 공포 분위기의<br>
엔터테인먼트 콘텐츠입니다.

<br><br>

실제 신점이나 미래를 예측하는 서비스가 아닙니다.

</div>
""",
            unsafe_allow_html=True
        )

# ============================================
# 하단 문구
# ============================================

st.markdown(
    """
<div class="footer">
    ─────────────────────────<br>
    당신이 이 페이지를 닫은 뒤에도<br>
    이름의 흔적은 잠시 남아 있을 것입니다.<br>
    ─────────────────────────
</div>
""",
    unsafe_allow_html=True
)

