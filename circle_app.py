import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Circle • Dubai", page_icon="🔥", layout="centered")

# === PREMIUM CSS (luxury glassmorphism 2026) ===
st.markdown("""
<style>
    .stApp { background: #0a0a0a; color: white; }
    .glass { background: rgba(255,255,255,0.07); backdrop-filter: blur(32px); 
              border-radius: 24px; border: 1px solid rgba(255,255,255,0.12); 
              box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.6); padding: 24px; }
    .gold { color: #d4af37; }
    .live { animation: pulse 2s infinite; }
    @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
    .title { font-family: 'Playfair Display', serif; letter-spacing: -0.06em; }
</style>
""", unsafe_allow_html=True)

# === SIDEBAR NAVIGATION ===
st.sidebar.markdown("<h1 class='title text-4xl gold'>Circle</h1>", unsafe_allow_html=True)
st.sidebar.caption("The Social OS for Dubai")

page = st.sidebar.radio("Навигация", 
    ["🏠 Energy", "🔍 Discover", "🌀 Circles", "🔥 Feed", "👤 Profile"],
    label_visibility="collapsed")

# === ONBOARDING (показывается один раз) ===
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if not st.session_state.onboarded:
    st.title("Добро пожаловать в Circle")
    st.subheader("Твой luxury круг в Дубае")
    st.write("**Build your real life through movement and meaningful people.**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Founder / Entrepreneur", use_container_width=True):
            st.session_state.onboarded = True
            st.rerun()
    with col2:
        if st.button("Русскоязычный экспат", use_container_width=True):
            st.session_state.onboarded = True
            st.rerun()
    if st.button("Premium Wellness", use_container_width=True):
        st.session_state.onboarded = True
        st.rerun()
    if st.button("Padel & Elite Community", use_container_width=True):
        st.session_state.onboarded = True
        st.rerun()
    st.stop()

# === MAIN PAGES ===
if page == "🏠 Energy":
    st.title("Доброе утро, Алексей 👋")
    st.markdown("<p class='gold text-xl'>341 человек в движении прямо сейчас <span class='live'>● LIVE</span></p>", unsafe_allow_html=True)
    
    st.markdown("### AI нашёл тебе идеального человека")
    if st.button("🔥 Посмотреть матч (97% совпадение)", type="primary", use_container_width=True):
        with st.expander("Дмитрий • Ex-YC Fintech Founder", expanded=True):
            st.write("1.4 км от тебя • Ищет партнёра на падел + разговор о раунде $3M")
            if st.button("Написать ему прямо сейчас"):
                st.success("Сообщение отправлено! Дмитрий ответил за 9 минут: «19:30 в Emirates Padel — идеально»")
    
    st.markdown("### Сейчас в городе")
    st.info("12 человек из твоего круга уже играют / бегают / нетворкают в Marina и Downtown")

elif page == "🔍 Discover":
    st.title("Найти людей")
    st.write("**AI-подобранные matches**")
    st.success("Анна • 34 • Wellness Founder\n\nИщет теннис-партнёра и разговор о масштабировании")
    if st.button("Отправить запрос на связь"):
        st.balloons()
        st.success("Запрос отправлен. Анна приняла его за 47 секунд!")

elif page == "🌀 Circles":
    st.title("Мои Circles")
    st.write("**Founders Padel Club** — ты Ambassador (Level 8)")
    st.write("**Russian Luxury Wellness** — 32 участника")
    st.button("Создать свой Circle", type="primary")

elif page == "🔥 Feed":
    st.title("Activity")
    st.write("Мария К. • только что")
    st.write("«Отличная игра и ещё лучшее продолжение в баре. Спасибо Circle за новые связи ❤️»")
    st.caption("— 11 человек уже лайкнули")

elif page == "👤 Profile":
    st.title("Твой профиль")
    st.markdown("<h2 class='gold'>Level 8 • Rising Luminary</h2>", unsafe_allow_html=True)
    st.metric("Social Capital", "2,840", "↑ 150 сегодня")
    st.write("Badges: Padel Elite • First Mover • Community Architect")
    st.button("Забрать ежедневную награду (+150 SC)")

# === FOOTER ===
st.sidebar.caption(f"🕒 {datetime.now().strftime('%H:%M')} • Dubai, UAE")
st.sidebar.caption("Готово для показа инвесторам")