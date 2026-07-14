  import streamlit as st
import random

# Настройка вкладки
st.set_page_config(page_title="Benteler Trainer: Feilen, Meißeln, Prüfen", page_icon="📐", layout="centered")

# Новая база данных вопросов
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = [
        {
            "question": "1. Wozu sollen die mit b gekennzeichneten spitzen, schneidenfoermigen Messflaechen des Messschiebers verwendet werden? (Bild 10/2)",
            "choices": [
                "a) Zum Anreissen von Lochteilen.",
                "b) Zum Anreissen von verzunderten Werkstuecken.",
                "c) Zum Messen von Bohrungsdurchmessern und Nutbreiten.",
                "d) Zum Messen von Kerndurchmessern bei Aussengewinden.",
                "e) Zum Messen von Nuttiefen bei Wellen."
            ],
            "correct": [
                "d) Zum Messen von Kerndurchmessern bei Aussengewinden."
            ]
        },
        {
            "question": "2. Welche Behauptung ueber die gekennzeichneten Teile (Bild 10/2 / erste Seite) des Messschiebers ist richtig?",
            "choices": [
                "a) Mit Teil k wird der bewegliche Messschenkel festgestellt.",
                "b) Auf Teil g liest man die vollen Millimeter ab.",
                "c) Die Teile a und h werden fuer Innenmessungen verwendet.",
                "d) Die Teile b werden fuer Aussenmessungen verwendet.",
                "e) Teil e wird zum Anreissen verwendet."
            ],
            "correct": [
                "a) Mit Teil k wird der bewegliche Messschenkel festgestellt."
            ]
        },
"question": "3. Wie groß ist die genormte Bezugstemperatur in der Längenprüftechnik?",
        "choices": [
            "a) 4°C",
            "b) 10°C",
            "c) 16°C",
            "d) 20°C",
            "e) 24°C"
        ],
        "correct": [
            "d) 20°C"
        ]
    },
    {
        "question": "4. Wie kann der Begriff „Messen“ erklärt werden?",
        "choices": [
            "a) Messen ist das Ermitteln von Nennmaßen mit gesetzlich vorgeschriebenem Maßstab.",
            "b) Messen ist das Ermitteln von absolut genauen Maßen.",
            "c) Messen ist das Überprüfen einer Maßtoleranz mit einer Lehre.",
            "d) Messen ist das Messen einer Länge oder eines Winkels mit einem Messgerät.",
            "e) Messen ist das Vergleichen eines Prüfgegenstandes mit einer Lehre."
        ],
        "correct": [
            "d) Messen ist das Messen einer Länge oder eines Winkels mit einem Messgerät."
        ]
    },
    {
        "question": "5. Welche Behauptung über das „Lehren“ ist richtig?",
        "choices": [
            "a) Beim Lehren werden sehr genaue Zahlenwerte ermittelt.",
            "b) Beim Lehren wird festgestellt, ob der Prüfgegenstand bestimmte Bedingungen erfüllt.",
            "c) Beim Lehren wird meist mit dem Messschieber gearbeitet.",
            "d) Lehren kann man nur mit dem Anschlagwinkel oder mit dem Haarlineal."
        ],
        "correct": [
            "b) Beim Lehren wird festgestellt, ob der Prüfgegenstand bestimmte Bedingungen erfüllt."
        ]
    },
    {
        "question": "6. Beim Messen mit dem Messschieber können Messfehler auftreten, Auf welche Fehlerquelle hat man beim Messen keinen Einfluss?",
        "choices": [
            "a) Ablesefehler durch Parallaxe",
            "b) Schmutz an den Messflächen des Messschiebers",
            "c) Schräges Ansetzen der Messschenkel",
            "d) Teilungsfehler des Nonius und der Strichskala",
            "e) Zu große Messkraft"
        ],
        "correct": [
            "d) Teilungsfehler des Nonius und der Strichskala."
        ]
    }
    {
        "question": "7. Wie ist die Ausschussseite eines Grenzlehrdorns gekennzeichnet?",
        "choices": [
            "a) Durch eine Fase",
            "b) Durch ein aufgestempeltes A",
            "c) Durch einen roten Farbring, außerdem ist diese Seite kürzer",
            "d) Durch die Beschriftung mit dem Nennmaß",
            "e) Durch eine Längsnut am Lehrenkörper"
        ],
        "correct": [
            "c) Durch einen roten Farbring, außerdem ist diese Seite kürzer"
        ]
    },
    {
        "question": "8. Welche Behauptung über das Prüfen mit der Grenzrachenlehre ist richtig?",
        "choices": [
            "a) Es wird das Istmaß gemessen",
            "b) Es wird festgestellt, ob das Istmaß innerhalb der zulässigen Toleranz liegt",
            "c) Es wird die Toleranz des Werkstücks gemessen",
            "d) Es wird das Größtmaß gemessen",
            "e) Es wird das Nennmaß gemessen"
        ],
        "correct": [
            "b) Es wird festgestellt, ob das Istmaß innerhalb der zulässigen Toleranz liegt"
        ]
    }
]
    
# Алгоритм перемешивания и логики
if "shuffled" not in st.session_state:
    q_list = list(st.session_state.quiz_data)
    random.shuffle(q_list)
    st.session_state.shuffled = q_list
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = []

st.title("📐 Feilen, Meißeln, Prüfen")
st.write("Benteler Fachkunde Trainer")
st.markdown("---")

if st.session_state.current_idx < len(st.session_state.shuffled):
    q = st.session_state.shuffled[st.session_state.current_idx]
    st.subheader(f"Frage {st.session_state.current_idx + 1} von {len(st.session_state.shuffled)}")
    st.info(q["question"])
    
    is_multiple = len(q["correct"]) > 1
    user_answers = []
    
    if is_multiple:
        st.caption("ℹ️ Mehrere Antworten auswaehlen:")
        for choice in q["choices"]:
            if st.checkbox(choice, key=f"c_{st.session_state.current_idx}_{choice}"):
                user_answers.append(choice)
    else:
        st.caption("ℹ️ Eine Antwort auswaehlen:")
        selected_radio = st.radio("Optionen:", q["choices"], index=None, key=f"r_{st.session_state.current_idx}", label_visibility="collapsed")
        user_answers = [selected_radio] if selected_radio else []

    if not st.session_state.answered:
        if st.button("Antworten", type="primary", use_container_width=True):
            if not user_answers:
                st.warning("Bitte waehlen Sie eine Antwort aus!")
            else:
                st.session_state.answered = True
                st.session_state.selected = user_answers
                st.rerun()
    else:
        correct_set = set(q["correct"])
        user_set = set(st.session_state.selected)
        
        if user_set == correct_set:
            st.success("🟢 Richtig!")
            if f"sc_{st.session_state.current_idx}" not in st.session_state:
                st.session_state.score += 1
                st.session_state[f"sc_{st.session_state.current_idx}"] = True
        else:
            st.error("🔴 Falsch!")
            st.write("**Richtige Antwort:**")
            for c in q["correct"]:
                st.write(f"✔️ {c}")
                
        if st.button("Naechste Frage ➡️", use_container_width=True):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.selected = []
            st.rerun()
else:
    st.success(f"🏁 Test beendet! Ihr Ergebnis: {st.session_state.score} von {len(st.session_state.shuffled)} richtig.")
    if st.button("Neu starten 🔄", use_container_width=True):
        del st.session_state.shuffled
        st.rerun()
