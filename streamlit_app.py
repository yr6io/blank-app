# streamlit_app.py

import streamlit as st
import random

# 1. 앱 페이지 기본 설정
st.set_page_config(
    page_title="숫자 맞추기 게임",
    page_icon="🔢"
)

# 2. 앱의 메인 제목 및 설명
st.title("🔢 숫자 맞추기 게임")
st.write("컴퓨터가 1부터 100까지의 숫자 중 하나를 정했습니다. 맞춰보세요! 👇")
st.markdown("---")

# 3. 게임 상태 초기화 및 관리 (세션 상태 사용)
# st.session_state는 Streamlit 앱이 재실행되어도 데이터를 유지할 수 있도록 도와줍니다.
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100) # 1부터 100까지의 숫자 중 하나를 선택
if 'guesses_made' not in st.session_state:
    st.session_state.guesses_made = 0 # 시도 횟수
if 'game_message' not in st.session_state:
    st.session_state.game_message = "숫자를 입력하고 '추측!' 버튼을 눌러주세요." # 게임 힌트 메시지
if 'game_over' not in st.session_state:
    st.session_state.game_over = False # 게임 종료 여부

# 4. 게임 규칙 및 진행 로직
def check_guess(guess):
    st.session_state.guesses_made += 1 # 시도 횟수 증가

    if guess < st.session_state.secret_number:
        st.session_state.game_message = "UP! 더 큰 숫자를 입력하세요. ⬆️"
    elif guess > st.session_state.secret_number:
        st.session_state.game_message = "DOWN! 더 작은 숫자를 입력하세요. ⬇️"
    else:
        st.session_state.game_message = f"🎉 정답입니다! {st.session_state.guesses_made}번 만에 맞추셨어요! 🎉"
        st.session_state.game_over = True # 게임 종료

# 5. 사용자 인터페이스 (UI) 구성
# 숫자를 입력받는 위젯
player_guess = st.number_input(
    "당신의 추측은?:",
    min_value=1,
    max_value=100,
    value=50, # 기본값 설정
    step=1,
    disabled=st.session_state.game_over, # 게임이 끝나면 입력 비활성화
    help="1부터 100 사이의 숫자를 입력하세요."
)

# 추측 버튼
if st.button("추측!", disabled=st.session_state.game_over, use_container_width=True):
    check_guess(player_guess)

st.markdown("---")

# 현재 게임 상태 메시지 표시
if st.session_state.game_over:
    st.success(st.session_state.game_message)
else:
    st.info(st.session_state.game_message)

# 시도 횟수 표시
st.write(f"현재 시도 횟수: **{st.session_state.guesses_made}**")

st.markdown("---")

# 게임 초기화 버튼
if st.button("새 게임 시작 🔄", type="primary", use_container_width=True):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guesses_made = 0
    st.session_state.game_message = "새 게임을 시작합니다! 다시 숫자를 맞춰보세요! 👇"
    st.session_state.game_over = False
    st.rerun() # 앱을 새로고침하여 상태를 초기화합니다. (st.experimental_rerun() -> st.rerun() 변경)
