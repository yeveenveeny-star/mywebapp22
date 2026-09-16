import streamlit as st
import random

# --------------------------------------------------
# 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="MBTI 여행지 추천 💕",
    page_icon="🌷",
    layout="centered"
)

# --------------------------------------------------
# 귀여운 CSS
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #fff7fb 0%, #f8f4ff 100%);
    }

    .main-title {
        text-align: center;
        color: #ff7eb6;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #8d7b9d;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .card {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 25px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 25px rgba(220, 170, 210, 0.18);
        border: 2px solid #ffe1ef;
    }

    .destination {
        color: #ff6fae;
        font-size: 30px;
        font-weight: 800;
        text-align: center;
    }

    .reason {
        color: #66556f;
        font-size: 17px;
        line-height: 1.7;
        text-align: center;
    }

    .tag {
        display: inline-block;
        background-color: #ffe5f0;
        color: #e85d9b;
        border-radius: 20px;
        padding: 6px 12px;
        margin: 3px;
        font-size: 14px;
    }

    .footer {
        text-align: center;
        color: #aaa0ad;
        font-size: 13px;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 여행지 데이터
# --------------------------------------------------
travel_data = {
    "INFP": [
        {
            "place": "교토 🇯🇵",
            "reason": "조용한 골목길을 천천히 걷고 예쁜 카페에서 감성 충전하기 좋아요.",
            "tags": ["감성여행", "카페", "고즈넉함"]
        },
        {
            "place": "제주도 🇰🇷",
            "reason": "푸른 바다와 예쁜 오름을 바라보며 나만의 시간을 보내기 딱 좋아요.",
            "tags": ["힐링", "자연", "감성"]
        },
        {
            "place": "파리 🇫🇷",
            "reason": "예술과 낭만이 가득한 도시에서 마음껏 상상하고 산책해 보세요.",
            "tags": ["예술", "낭만", "산책"]
        }
    ],

    "ENFP": [
        {
            "place": "방콕 🇹🇭",
            "reason": "맛있는 음식부터 야시장, 쇼핑까지 신나는 경험이 가득해요!",
            "tags": ["맛집", "쇼핑", "액티비티"]
        },
        {
            "place": "런던 🇬🇧",
            "reason": "새로운 사람과 문화, 볼거리를 만나는 재미가 쏠쏠한 도시예요.",
            "tags": ["문화", "도시", "모험"]
        },
        {
            "place": "부산 🇰🇷",
            "reason": "바다도 보고 맛있는 것도 먹고 밤에는 신나게 놀아봐요!",
            "tags": ["바다", "맛집", "놀거리"]
        }
    ],

    "INFJ": [
        {
            "place": "후쿠오카 🇯🇵",
            "reason": "여유로운 분위기 속에서 맛있는 음식과 작은 행복을 발견할 수 있어요.",
            "tags": ["힐링", "소도시", "맛집"]
        },
        {
            "place": "스위스 🇨🇭",
            "reason": "웅장한 자연을 바라보며 마음을 정리하고 재충전하기 좋아요.",
            "tags": ["자연", "힐링", "풍경"]
        },
        {
            "place": "경주 🇰🇷",
            "reason": "역사와 고즈넉한 풍경 속에서 천천히 생각에 잠겨보세요.",
            "tags": ["역사", "고즈넉함", "산책"]
        }
    ],

    "ENFJ": [
        {
            "place": "하와이 🇺🇸",
            "reason": "사랑하는 사람들과 함께라면 행복이 두 배! 바다와 액티비티를 즐겨보세요.",
            "tags": ["휴양", "친구", "바다"]
        },
        {
            "place": "파리 🇫🇷",
            "reason": "사람들과 함께 아름다운 풍경과 맛있는 음식을 즐기기 좋은 곳이에요.",
            "tags": ["낭만", "문화", "맛집"]
        },
        {
            "place": "서울 🇰🇷",
            "reason": "친구들과 맛집, 카페, 쇼핑을 모두 즐길 수 있는 다채로운 여행지예요.",
            "tags": ["도시", "쇼핑", "친구"]
        }
    ],

    "INTP": [
        {
            "place": "도쿄 🇯🇵",
            "reason": "첨단 기술부터 독특한 서브컬처까지 호기심을 자극하는 것이 가득해요.",
            "tags": ["테크", "서브컬처", "탐험"]
        },
        {
            "place": "싱가포르 🇸🇬",
            "reason": "깔끔하고 독특한 도시 시스템과 다양한 문화를 탐험해 보세요.",
            "tags": ["도시", "문화", "탐험"]
        },
        {
            "place": "대전 🇰🇷",
            "reason": "과학과 연구의 도시에서 색다른 여행의 재미를 찾아보세요.",
            "tags": ["과학", "도시", "탐구"]
        }
    ],

    "ENTP": [
        {
            "place": "뉴욕 🇺🇸",
            "reason": "매일 새로운 일이 벌어지는 곳! 지루할 틈 없이 도시를 탐험해 보세요.",
            "tags": ["도시", "문화", "모험"]
        },
        {
            "place": "홍콩 🇭🇰",
            "reason": "복잡하고 빠르게 움직이는 도시에서 새로운 자극을 마음껏 받아보세요.",
            "tags": ["야경", "맛집", "도시"]
        },
        {
            "place": "부산 🇰🇷",
            "reason": "바다부터 시장, 카페까지 예상하지 못한 재미를 발견하기 좋아요.",
            "tags": ["바다", "탐험", "먹방"]
        }
    ],

    "INTJ": [
        {
            "place": "스위스 🇨🇭",
            "reason": "정교하게 계획한 일정과 아름다운 자연을 함께 즐길 수 있어요.",
            "tags": ["자연", "계획", "풍경"]
        },
        {
            "place": "도쿄 🇯🇵",
            "reason": "효율적인 도시 시스템과 다양한 볼거리를 체계적으로 탐험해 보세요.",
            "tags": ["효율", "도시", "문화"]
        },
        {
            "place": "제주도 🇰🇷",
            "reason": "렌터카로 원하는 장소를 직접 계획해서 돌아보기 좋아요.",
            "tags": ["자유여행", "자연", "계획"]
        }
    ],

    "ENTJ": [
        {
            "place": "뉴욕 🇺🇸",
            "reason": "빠르고 역동적인 도시에서 쇼핑과 미식, 문화생활을 모두 즐겨보세요.",
            "tags": ["도시", "쇼핑", "미식"]
        },
        {
            "place": "싱가포르 🇸🇬",
            "reason": "깔끔하고 효율적인 도시를 알차게 돌아다니는 여행이 잘 어울려요.",
            "tags": ["도시", "효율", "미식"]
        },
        {
            "place": "서울 🇰🇷",
            "reason": "빠르게 변화하는 도시에서 새로운 트렌드를 경험해 보세요.",
            "tags": ["트렌드", "도시", "쇼핑"]
        }
    ],

    "ISFP": [
        {
            "place": "제주도 🇰🇷",
            "reason": "예쁜 바다와 자연을 바라보며 천천히 나만의 여행을 즐겨보세요.",
            "tags": ["자연", "감성", "힐링"]
        },
        {
            "place": "오키나와 🇯🇵",
            "reason": "따뜻한 햇살과 푸른 바다 속에서 여유로운 시간을 보내기 좋아요.",
            "tags": ["바다", "휴양", "감성"]
        },
        {
            "place": "통영 🇰🇷",
            "reason": "작고 예쁜 항구 도시에서 맛있는 음식과 풍경을 즐겨보세요.",
            "tags": ["바다", "소도시", "맛집"]
        }
    ],

    "ESFP": [
        {
            "place": "부산 🇰🇷",
            "reason": "바다에서 놀고 맛있는 것도 먹고 신나게 즐겨봐요!",
            "tags": ["바다", "먹방", "액티비티"]
        },
        {
            "place": "방콕 🇹🇭",
            "reason": "화려한 야시장과 맛있는 음식, 쇼핑까지 재미있는 게 너무 많아요!",
            "tags": ["야시장", "맛집", "쇼핑"]
        },
        {
            "place": "하와이 🇺🇸",
            "reason": "햇살 가득한 해변에서 신나게 놀고 인생 사진도 남겨보세요.",
            "tags": ["휴양", "바다", "사진"]
        }
    ],

    "ISFJ": [
        {
            "place": "후쿠오카 🇯🇵",
            "reason": "편안하고 아늑한 분위기에서 맛있는 음식과 소소한 행복을 즐겨보세요.",
            "tags": ["힐링", "맛집", "소도시"]
        },
        {
            "place": "경주 🇰🇷",
            "reason": "천천히 걸으며 아름다운 문화유산을 구경하기 좋아요.",
            "tags": ["역사", "산책", "힐링"]
        },
        {
            "place": "교토 🇯🇵",
            "reason": "차분한 분위기 속에서 전통적인 일본의 매력을 느껴보세요.",
            "tags": ["전통", "산책", "감성"]
        }
    ],

    "ESFJ": [
        {
            "place": "파리 🇫🇷",
            "reason": "친구나 가족과 함께 맛있는 음식과 아름다운 풍경을 즐겨보세요.",
            "tags": ["가족", "맛집", "낭만"]
        },
        {
            "place": "서울 🇰🇷",
            "reason": "사람들과 함께 맛집과 카페, 쇼핑을 즐기기에 최고의 도시예요.",
            "tags": ["친구", "맛집", "쇼핑"]
        },
        {
            "place": "후쿠오카 🇯🇵",
            "reason": "맛있는 음식과 편안한 여행 분위기로 함께 가는 사람도 행복해져요.",
            "tags": ["맛집", "친구", "힐링"]
        }
    ],

    "ISTP": [
        {
            "place": "제주도 🇰🇷",
            "reason": "렌터카를 타고 마음 가는 곳으로 떠나는 자유로운 여행을 즐겨보세요.",
            "tags": ["드라이브", "자유", "자연"]
        },
        {
            "place": "뉴질랜드 🇳🇿",
            "reason": "광활한 자연 속에서 액티비티와 모험을 즐길 수 있어요.",
            "tags": ["자연", "모험", "액티비티"]
        },
        {
            "place": "오키나와 🇯🇵",
            "reason": "바다에서 다양한 액티비티를 즐기며 자유롭게 돌아다녀 보세요.",
            "tags": ["바다", "자유", "액티비티"]
        }
    ],

    "ESTP": [
        {
            "place": "라스베이거스 🇺🇸",
            "reason": "화려한 볼거리와 다양한 액티비티로 에너지를 마음껏 발산해 보세요.",
            "tags": ["액티비티", "화려함", "도시"]
        },
        {
            "place": "방콕 🇹🇭",
            "reason": "먹고 쇼핑하고 돌아다니며 도시의 에너지를 제대로 느껴보세요.",
            "tags": ["먹방", "쇼핑", "모험"]
        },
        {
            "place": "부산 🇰🇷",
            "reason": "바다와 맛집과 다양한 놀거리를 한 번에 즐길 수 있어요.",
            "tags": ["바다", "맛집", "놀거리"]
        }
    ],

    "ISTJ": [
        {
            "place": "교토 🇯🇵",
            "reason": "정돈된 여행 일정으로 전통적인 명소들을 차근차근 둘러보기 좋아요.",
            "tags": ["전통", "계획", "문화"]
        },
        {
            "place": "싱가포르 🇸🇬",
            "reason": "깔끔하고 체계적인 도시를 편안하게 여행할 수 있어요.",
            "tags": ["깔끔함", "도시", "문화"]
        },
        {
            "place": "경주 🇰🇷",
            "reason": "역사적인 장소들을 하나씩 둘러보며 의미 있는 여행을 만들어 보세요.",
            "tags": ["역사", "문화", "계획"]
        }
    ],

    "ESTJ": [
        {
            "place": "서울 🇰🇷",
            "reason": "볼거리와 먹거리, 쇼핑을 효율적으로 정리해서 알차게 여행할 수 있어요.",
            "tags": ["도시", "쇼핑", "효율"]
        },
        {
            "place": "도쿄 🇯🇵",
            "reason": "효율적인 교통과 다양한 관광지를 활용해 꽉 찬 여행을 만들어 보세요.",
            "tags": ["도시", "계획", "쇼핑"]
        },
        {
            "place": "싱가포르 🇸🇬",
            "reason": "깨끗하고 체계적인 도시에서 계획적인 여행을 즐겨보세요.",
            "tags": ["계획", "도시", "깔끔함"]
        }
    ]
}

# --------------------------------------------------
# 화면
# --------------------------------------------------
st.markdown(
    '<div class="main-title">🌷 MBTI 여행지 추천 🌷</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">나의 MBTI와 찰떡궁합인 여행지를 찾아볼까요? ✈️💕</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">
    <h3 style="text-align:center; color:#ff80b5;">
        💌 여행을 떠나기 전에...
    </h3>
    <p style="text-align:center; color:#777;">
        당신의 MBTI를 골라주세요!<br>
        귀여운 여행 추천 요정이 여행지를 골라드릴게요 🧚‍♀️✨
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MBTI 선택
# --------------------------------------------------
mbti_list = [
    "INFP", "ENFP", "INFJ", "ENFJ",
    "INTP", "ENTP", "INTJ", "ENTJ",
    "ISFP", "ESFP", "ISFJ", "ESFJ",
    "ISTP", "ESTP", "ISTJ", "ESTJ"
]

mbti = st.selectbox(
    "💗 나의 MBTI는?",
    mbti_list,
    index=0
)

st.markdown("")

# --------------------------------------------------
# 추천 버튼
# --------------------------------------------------
if st.button("🎀 나에게 딱 맞는 여행지 찾기 🎀", use_container_width=True):

    destination = random.choice(travel_data[mbti])

    st.balloons()

    st.markdown("""
    <div class="card">
        <div style="text-align:center; font-size:45px;">🎉</div>
        <div style="text-align:center; color:#9b7aaa; font-size:18px;">
            당신에게 추천하는 여행지는...
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="card">
            <div class="destination">{destination["place"]}</div>
            <br>
            <div class="reason">{destination["reason"]}</div>
            <br>
            <div style="text-align:center;">
                {" ".join(
                    f'<span class="tag">#{tag}</span>'
                    for tag in destination["tags"]
                )}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card">
            <p style="text-align:center; color:#777;">
                💕 <b>{mbti}</b> 여행자님을 위한 작은 여행 팁 💕
            </p>
            <p style="text-align:center; color:#8d7b9d;">
                너무 완벽하게 계획하지 말고,<br>
                여행지에서 우연히 만나는 순간도 마음껏 즐겨보세요! 🌸
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# 다시 뽑기
# --------------------------------------------------
st.markdown(
    '<div class="footer">🌸 MBTI 여행지 추천 요정이 당신의 행복한 여행을 응원해요 🌸</div>',
    unsafe_allow_html=True
)
