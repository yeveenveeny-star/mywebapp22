import streamlit as st
import random
import hashlib
import time

# ==========================================
# 페이지 설정
# ==========================================
st.set_page_config(
    page_title="그 이름을 입력하지 마세요...",
    page_icon="👁️",
    layout="centered"
)

# ==========================================
# CSS - 어둡고 무서운 분위기
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Noto+Sans+KR:wght@400;700&display=swap');

    .stApp {
        background:
            radial-gradient(circle at 50% 20%, #24111c 0%, #0d080c 35%, #030304 100%);
        color: #ddd;
    }

    .main-title {
        text-align: center;
        font-family: 'Cinzel', serif;
        font-size: 42px;
        font-weight: 700;
        color: #d8a0ad;
        text-shadow:
            0 0 8px #8f263f,
            0 0 20px #5a1025;
        margin-top: 20px;
    }

    .warning {
        text-align: center;
        color: #8e6872;
        font-size: 14px;
        letter-spacing: 2px;
        margin-bottom: 35px;
    }

    .eye {
        text-align: center;
        font-size: 70px;
        color: #8f263f;
        text-shadow: 0 0 25px #b92f50;
        margin-bottom: -10px;
    }

    .input-card {
        background: rgba(20, 12, 17, 0.9);
        border: 1px solid #49202d;
        border-radius: 8px;
        padding: 28px;
        box-shadow:
            0 0 30px rgba(110, 20, 50, 0.15),
            inset 0 0 20px rgba(0,0,0,0.5);
        margin-bottom: 25px;
    }

    .result-card {
        background:
            linear-gradient(
                135deg,
                rgba(28, 13, 20, 0.98),
                rgba(8, 7, 10, 0.98)
            );
        border: 1px solid #642639;
        border-radius: 5px;
        padding: 30px;
        margin-top: 25px;
        box-shadow:
            0 0 35px rgba(130, 20, 55, 0.25),
            inset 0 0 30px rgba(0,0,0,0.6);
    }

    .name-result {
        text-align: center;
        color: #c77c8e;
        font-size: 20px;
        margin-bottom: 10px;
    }

    .fortune-title {
        text-align: center;
        color: #e4b5bf;
        font-size: 28px;
        font-weight: bold;
        margin: 10px 0 25px;
        text-shadow: 0 0 10px #712238;
    }

    .fortune-text {
        color: #c8b7bc;
        font-size: 17px;
        line-height: 2;
        text-align: center;
    }

    .red-text {
        color: #b43b57;
        font-weight: bold;
    }

    .small-warning {
        text-align: center;
        color: #66535a;
        font-size: 12px;
        margin-top: 30px;
        line-height: 1.8;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #501728, #781d37);
        color: #ead5da;
        border: 1px solid #8c3048;
        border-radius: 4px;
        font-size: 17px;
        padding: 12px;
        transition: all 0.3s;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #721d36, #a32a4b);
        color: white;
        box-shadow: 0 0 20px rgba(170, 35, 70, 0.4);
    }

    input {
        background-color: #100b0e !important;
        color: #e0cbd0 !important;
        border: 1px solid #4a2630 !important;
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
</style>
""", unsafe_allow_html=True)


# ==========================================
# 데이터
# ==========================================

omens = [
    {
        "title": "붉은 달의 기운",
        "message": "당신의 이름에는 이상하게도 붉은 기운이 남아 있습니다. "
                   "가까운 시일 안에 잊고 있던 사람이나 장소를 다시 마주하게 될 수 있습니다.",
        "warning": "특히 밤늦게 걸려오는 전화 한 통을 조심하세요."
    },
    {
        "title": "문 뒤에 남은 기척",
        "message": "당신 주변에 아직 끝나지 않은 일이 하나 있습니다. "
                   "이미 지나갔다고 생각했던 일이 다른 모습으로 다시 나타날 수 있습니다.",
        "warning": "혼자 있을 때 문밖에서 나는 작은 소리에 귀를 기울이지 마세요."
    },
    {
        "title": "검은 실",
        "message": "당신의 이름을 따라 아주 가느다란 인연의 실이 이어져 있습니다. "
                   "끊어진 줄 알았던 관계가 다시 이어질 가능성이 보입니다.",
        "warning": "오래 연락하지 않은 사람의 이름을 먼저 부르지는 마세요."
    },
    {
        "title": "새벽 3시의 그림자",
        "message": "당신의 기운에는 밤의 흔적이 강하게 남아 있습니다. "
                   "새벽에 갑자기 눈을 뜨는 날이 있다면 주변을 천천히 둘러보세요.",
        "warning": "그 시간에는 거울을 오래 바라보지 않는 것이 좋습니다."
    },
    {
        "title": "뒤돌아보지 마세요",
        "message": "당신에게는 앞으로 나아가는 기운과 뒤에서 붙잡는 기운이 동시에 보입니다. "
                   "과거의 선택에 대한 생각이 갑자기 강해질 수 있습니다.",
        "warning": "밤길에서 누군가 부르는 것 같아도 바로 뒤돌아보지는 마세요."
    },
    {
        "title": "빈 의자",
        "message": "당신의 운세에는 이상하게도 '자리'라는 상징이 반복됩니다. "
                   "누군가 떠난 자리에 새로운 인연이 들어오는 흐름입니다.",
        "warning": "혼자 있는 방에서 의자를 마주 보고 오래 앉아 있지는 마세요."
    },
    {
        "title": "이름을 부르는 소리",
        "message": "당신의 이름은 소리로 불렸을 때 특별한 기운을 갖습니다. "
                   "가까운 시기에 누군가가 예상하지 못한 순간 당신의 이름을 부르게 됩니다.",
        "warning": "처음 듣는 목소리라면 대답하기 전에 잠시 멈추세요."
    },
    {
        "title": "닫힌 문",
        "message": "현재 당신 앞에는 하나의 닫힌 문이 보입니다. "
                   "하지만 그 문은 막힌 것이 아니라 아직 열 때가 되지 않은 문입니다.",
        "warning": "급하게 결정하지 마세요. 이상하게 마음에 걸리는 선택은 하루 정도 미뤄보세요."
    }
]

# ==========================================
# 이름 기반 랜덤 선택
# ==========================================

def get_result(name):
    """
    같은 이름을 입력하면 어느 정도 일관된 결과가 나오도록
    이름을 해시값으로 변환합니다.
    """
    seed_value = int(
        hashlib.sha256(name.encode("utf-8")).hexdigest(),
        16
    )

    rng = random.Random(seed_value)

    omen = rng.choice(omens)

    numbers = [
        rng.randint(1, 9),
        rng.randint(1, 9),
        rng.randint(1, 9)
    ]

    symbols = [
        "달 🌙",
        "까마귀 🐦‍⬛",
        "붉은 꽃 🥀",
        "열쇠 🗝️",
        "거울 🪞",
        "초승달 🌘",
        "검은 나비 🦋"
    ]

    symbol = rng.choice(symbols)

    return omen, numbers, symbol


# ==========================================
# 메인 화면
# ==========================================

st.markdown(
    '<div class="eye">👁️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">그 이름을<br>입력하지 마세요...</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="warning">당신의 이름을 알고 있습니다.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="input-card">
    <p style="
        text-align:center;
        color:#a98992;
        font-size:15px;
        letter-spacing:1px;
    ">
        이름을 입력하면<br>
        당신에게 남아 있는 기운을 읽어드립니다.
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 이름 입력
# ==========================================

name = st.text_input(
    "이름",
    placeholder="당신의 이름을 입력하세요...",
    label_visibility="collapsed"
)

st.markdown("")


# ==========================================
# 버튼
# ==========================================

if st.button(
    "👁️ 내 이름의 기운을 확인한다",
    use_container_width=True
):

    if not name.strip():
        st.warning("이름을 입력하세요.")

    else:
        # 로딩 연출
        with st.spinner("이름의 흔적을 읽고 있습니다..."):
            time.sleep(1.2)

        omen, numbers, symbol = get_result(name.strip())

        st.markdown(
            f"""
            <div class="result-card">

                <div class="name-result">
                    「 {name.strip()} 」
                </div>

                <div class="divider"></div>

                <div class="fortune-title">
                    {omen["title"]}
                </div>

                <div class="fortune-text">
                    {omen["message"]}
                </div>

                <div class="divider"></div>

                <div style="
                    text-align:center;
                    color:#80656e;
                    font-size:14px;
                ">
                    오늘의 기운을 상징하는 것
                </div>

                <div style="
                    text-align:center;
                    font-size:35px;
                    margin:15px;
                ">
                    {symbol}
                </div>

                <div style="
                    text-align:center;
                    color:#9b7881;
                    letter-spacing:8px;
                    font-size:18px;
                ">
                    {" · ".join(map(str, numbers))}
                </div>

                <div class="divider"></div>

                <div class="small-warning">
                    ⚠ {omen["warning"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="small-warning">
            ─────────────────────<br>
            이 결과는 공포 콘셉트의 엔터테인먼트 콘텐츠입니다.<br>
            실제 미래나 초자연적인 현상을 예측하는 것은 아닙니다.
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 하단
# ==========================================

st.markdown("""
<div style="
    text-align:center;
    margin-top:50px;
    color:#3e3035;
    font-size:11px;
">
    당신이 이 페이지를 닫은 뒤에도<br>
    이름은 한동안 남아 있을 것입니다.
</div>
""", unsafe_allow_html=True)
