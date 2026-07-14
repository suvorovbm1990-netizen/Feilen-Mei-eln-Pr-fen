import streamlit as st
import random

# Настройка вкладки
st.set_page_config(page_title="Benteler Trainer: Feilen, Meißeln, Prüfen", page_icon="📐", layout="centered")

# Ссылка на твой репозиторий для загрузки картинок
GITHUB_RAW_URL = "https://raw.githubusercontent.com/suvorovbm1990-netizen/Feilen-Mei-eln-Pr-fen/main/"

# База данных вопросов
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = [
        # ВОПРОС 1: ДЕТАЛИ ШТАНГЕНЦИРКУЛЯ (с картинкой)
        {
            "question": "1. Benennen Sie die Teile des Messschiebers (Bild 10/2):",
            "type": "text_input",
            "image": "messschieber.png",
            "inputs": {
                "a": ["fester messschenkel", "feststehender messschenkel"],
                "b": ["messspitzen für innenmesungen", "messspitzen für innenmessungen", "schneidenförmige messflächen", "messflächen für innenmessungen"],
                "c": ["schieber"],
                "d": ["hauptmaßstab", "schiene", "strichskala"],
                "e": ["tiefenmassstange", "tiefenmaßstange", "tiefenmaß", "tiefenmessstift"],
                "f": ["messfläche für tiefenmessung", "messfläche für tiefenmessungen", "messfläche"],
                "g": ["nonius", "noniusskala"],
                "h": ["bewegliches messschenkel", "beweglicher messschenkel"],
                "i": ["messflächen für außenmesungen", "messflächen für außenmessungen", "messflächen für aussenmessungen", "feststehender messschenkel"],
                "k": ["klemschraube", "klemmschraube", "feststellschraube"]
            }
        },
        # ВОПРОС 15: ДЕТАЛИ НАПИЛЬНИКА (с картинкой)
        {
            "question": "15. Benennen Sie die gekennzeichneten Bestandteile der Feile (Bild 6/1):",
            "type": "text_input",
            "image": "feile.png",
            "inputs": {
                "a": ["feilenkörper", "feilenkoerper", "feilen koper", "feilenblatt"],
                "b": ["angel", "feilenangel"],
                "c": ["feilengriff", "heft", "griff"]
            }
        },
        # ВОПРОС 16: НОМЕРА НАСЕЧЕК (HIEBNUMMERN)
        {
            "question": "16. Wozu benutzt man Feilen mit folgenden Hiebnummern:",
            "type": "text_input",
            "inputs": {
                "hiebnummer 1": ["schruppen", "grobe arbeiten", "grobe bearbeitung"],
                "hiebnummer 2": ["schlichten", "halbschlichten", "mittlere arbeiten"],
                "hiebnummer 3": ["feinschlichten", "schlichten", "feine arbeiten"],
                "hiebnummer 4": ["feinschlichten", "feinstschlichten", "sehr feine arbeiten", "schlichten von passungen"]
            }
        },
        # ВОПРОС 17: ТЕХНИКА БЕЗОПАСНОСТИ (ЧЕКБОКСЫ)
        {
            "question": "17. Welche der folgenden Maßnahmen dienen der Unfallverhütung beim Feilen? (Mehrere Antworten richtig)",
            "type": "choice",
            "choices": [
                "a) Nur Feilen mit fest sitzendem und unbeschädigtem Griff verwenden.",
                "b) Feilenspäne mit dem Mund wegblasen, um Zeit zu sparen.",
                "c) Niemals eine Feile ohne Griff (mit nackter Angel) benutzen.",
                "d) Feilenspäne только с помощью щетки (Handfeger/Bürste) убирать.",
                "e) Das Werkstück immer fest und sicher im Schraubstock einspannen.",
                "f) Die Feile mit Öl schmieren, damit sie besser gleitet."
            ],
            "correct": [
                "a) Nur Feilen mit fest sitzendem und unbeschädigtem Griff verwenden.",
                "c) Niemals eine Feile ohne Griff (mit nackter Angel) benutzen.",
                "d) Feilenspäne только с помощью щетки (Handfeger/Bürste) убирать.",
                "e) Das Werkstück immer fest und sicher im Schraubstock einspannen."
            ]
        },
        # ОСТАЛЬНЫЕ ВОПРОСЫ
        {
            "question": "2. Wozu sollen die mit b gekennzeichneten spitzen, schneidenfoermigen Messflaechen des Messschiebers verwendet werden? (Bild 10/2)",
            "type": "choice",
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
            "question": "3. Welche Behauptung ueber die gekennzeichneten Teile (Bild 10/2 / erste Seite) des Messschiebers is richtig?",
            "type": "choice",
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
        {
            "question": "4. Wie groß ist die genormte Bezugstemperatur in der Längenprüftechnik?",
            "type": "choice",
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
            "question": "5. Wie kann der Begriff „Messen“ erklärt werden?",
            "type": "choice",
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
            "question": "6. Welche Behauptung über das „Lehren“ is richtig?",
            "type": "choice",
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
            "question": "7. Beim Messen mit dem Messschieber können Messfehler auftreten. Auf welche Fehlerquelle hat man beim Messen keinen Einfluss?",
            "type": "choice",
            "choices": [
                "a) Ablesefehler durch Parallaxe",
                "b) Schmutz an den Messflächen des Messschiebers",
                "c) Schräges Ansetzen der Messschenkel",
                "d) Teilungsfehler des Nonius und der Strichskala",
                "e) Zu große Messkraft"
            ],
            "correct": [
                "d) Teilungsfehler des Nonius und der Strichskala"
            ]
        },
        {
            "question": "8. Wie ist die Ausschussseite eines Grenzlehrdorns gekennzeichnet?",
            "type": "choice",
            "choices": [
                "a) Durch eine Fase",
                "b) Durch ein aufgestempeltes A",
                "c) Durch einen roten Farbring, außerdem ist diese Seite kürzer",
                "d) Durch die Beschriftung with dem Nennmaß",
                "e) Durch eine Längsnut am Lehrenkörper"
            ],
            "correct": [
                "c) Durch einen roten Farbring, außerdem ist diese Seite kürzer"
            ]
        },
        {
            "question": "9. Welche Behauptung über das Prüfen mit der Grenzrachenlehre ist richtig?",
            "type": "choice",
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

# Перемешивание вопросов
if "shuffled" not in st.session_state:
    q_list = list(st.session_state.quiz_data)
    random.shuffle(q_list)
    st.session_state.shuffled = q_list
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = {}

st.title("📐 Feilen, Meißeln, Prüfen")
st.write("Benteler Fachkunde Trainer")
st.markdown("---")

if st.session_state.current_idx < len(st.session_state.shuffled):
    q = st.session_state.shuffled[st.session_state.current_idx]
    st.subheader(f"Frage {st.session_state.current_idx + 1} von {len(st.session_state.shuffled)}")
    st.info(q["question"])
    
    # Отображение картинки, если она добавлена к вопросу
    if "image" in q:
        image_url = GITHUB_RAW_URL + q["image"]
        st.image(image_url, use_container_width=True)
    
    q_type = q.get("type", "choice")
    user_answers = {}

    # Рендеринг в зависимости от типа вопроса
    if q_type == "text_input":
        st.write("Geben Sie die korrekten Bezeichnungen ein:")
        col1, col2 = st.columns(2)
        keys = list(q["inputs"].keys())
        
        for i, key in enumerate(keys):
            target_col = col1 if i < len(keys)/2 else col2
            with target_col:
                user_answers[key] = st.text_input(f"{key.upper()} =", key=f"text_{st.session_state.current_idx}_{key}").strip().lower()
                
    else: # Обычный тест или тест с чекбоксами (несколько вариантов)
        is_multiple = len(q["correct"]) > 1
        if is_multiple:
            st.caption("ℹ️ Mehrere Antworten auswählen (Отметьте правильные варианты):")
            selected_list = []
            for choice in q["choices"]:
                if st.checkbox(choice, key=f"c_{st.session_state.current_idx}_{choice}"):
                    selected_list.append(choice)
            user_answers["choice"] = selected_list
        else:
            st.caption("ℹ️ Eine Antwort auswählen (Выберите один вариант):")
            selected_radio = st.radio("Optionen:", q["choices"], index=None, key=f"r_{st.session_state.current_idx}", label_visibility="collapsed")
            user_answers["choice"] = [selected_radio] if selected_radio else []

    # Логика кнопок проверки
    if not st.session_state.answered:
        if st.button("Antworten", type="primary", use_container_width=True):
            if q_type == "text_input":
                empty = any(val == "" for val in user_answers.values())
                if empty:
                    st.warning("Bitte füllen Sie alle Felder aus!")
                else:
                    st.session_state.answered = True
                    st.session_state.selected = user_answers
                    st.rerun()
            else:
                if not user_answers["choice"]:
                    st.warning("Bitte wählen Sie eine Antwort aus!")
                else:
                    st.session_state.answered = True
                    st.session_state.selected = user_answers
                    st.rerun()
    else:
        # Показ результатов проверки
        if q_type == "text_input":
            all_correct = True
            st.write("### Ergebnisse der Überprüfung:")
            
            for key, accepted_answers in q["inputs"].items():
                user_val = st.session_state.selected.get(key, "")
                if user_val in accepted_answers:
                    st.success(f"✔️ **{key.upper()}**: {user_val.capitalize()}")
                else:
                    all_correct = False
                    st.error(f"❌ **{key.upper()}**: Ваш ответ: '{user_val}'. Ожидалось: {accepted_answers[0].capitalize()}")
            
            if all_correct:
                st.success("🟢 Alle Antworten sind richtig!")
                if f"sc_{st.session_state.current_idx}" not in st.session_state:
                    st.session_state.score += 1
                    st.session_state[f"sc_{st.session_state.current_idx}"] = True
            else:
                st.error("🔴 Einige Antworten sind falsch.")
                
        else:
            correct_set = set(q["correct"])
            user_set = set(st.session_state.selected.get("choice", []))
            
            if user_set == correct_set:
                st.success("🟢 Richtig!")
                if f"sc_{st.session_state.current_idx}" not in st.session_state:
                    st.session_state.score += 1
                    st.session_state[f"sc_{st.session_state.current_idx}"] = True
            else:
                st.error("🔴 Falsch!")
                st.write("**Richtige Antwort(en):**")
                for c in q["correct"]:
                    st.write(f"✔️ {c}")
                    
        if st.button("Nächste Frage ➡️", use_container_width=True):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.selected = {}
            st.rerun()
else:
    st.success(f"🏁 Test beendet! Ihr Ergebnis: {st.session_state.score} von {len(st.session_state.shuffled)} richtig.")
    if st.button("Neu starten 🔄", use_container_width=True):
        del st.session_state.shuffled
        st.rerun()
