import streamlit as st
import random
import os

# Настройка вкладки
st.set_page_config(page_title="Benteler Trainer: Feilen, Meißeln, Prüfen", page_icon="📐", layout="centered")

# База данных вопросов
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = [
        # ВОПРОС 1: ДЕТАЛИ ШТАНГЕНЦИРКУЛЯ
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
        # ВОПРОС 11: BÜGELMESSSCHRAUBE
        {
            "question": "11. Benennen Sie die Teile der Bügelmessschraube (Bild 10/22):",
            "type": "text_input",
            "image": "buegelmessschraube.jpeg",
            "inputs": {
                "a": ["bügel", "buegel"],
                "b": ["amboss"],
                "c": ["messspindel"],
                "d": ["feststellung"],
                "e": ["messhülse", "messhuelse", "skalenhülse", "skalenhuelse", "hauptmaßstab"],
                "f": ["messtrommel", "skalentrommel"],
                "g": ["kupplung", "ratsche"],
                "h": ["isolierplatte", "wärmeschutz", "waermeschutz"]
            }
        },
        # ВОПРОС 15: ДЕТАЛИ НАПИЛЬНИКА
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
        # ВОПРОС 16: НОМЕРА НАСЕЧЕК
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
        # ВОПРОС 17: ТЕХНИКА БЕЗОПАСНОСТИ (ввод 4 из 6)
        {
            "question": "17. Nennen Sie vier wichtige Maßnahmen zur Unfallverhütung beim Feilen:",
            "type": "unfall_inputs",
            "hint_options": [
                "1. Nicht ohne Feilengriff feilen.",
                "2. Keinen beschädigten Feilengriff verwenden.",
                "3. Feilengriff fest eintauchen.",
                "4. Späne nicht wegblasen.",
                "5. Das Werkstück fest einspannen.",
                "6. Nach dem Feilen Werkstück entgraten."
            ],
            "accepted_rules": [
                ["nicht ohne feilengriff feilen", "nicht ohne griff feilen", "nicht ohne feilengriff"],
                ["keinen beschädigten feilengriff verwenden", "keinen beschaedigten feilengriff verwenden", "keinen beschädigten griff verwenden", "keine besätigen feilengriff verwenden"],
                ["feilengriff fest eintauchen", "feilengriff fest aufsetzen", "griff fest eintauchen"],
                ["späne nicht wegblasen", "spaene nicht wegblasen", "spene nicht wegblasen"],
                ["das werkstück fest einspannen", "das werkstueck fest einspannen", "werkstück fest einspannen", "werkstueck fest einspannen"],
                ["nach dem feilen werkstück entgraten", "nach dem werkstück entgraten", "nach dem feilen werkstueck entgraten", "werkstück entgraten"]
            ]
        },
        # ВОПРОС 2: НАЗНАЧЕНИЕ ГУБОК (ИСПРАВЛЕН ПРАВИЛЬНЫЙ ОТВЕТ!)
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
                "c) Zum Messen von Bohrungsdurchmessern und Nutbreiten."
            ]
        },
        # ВОПРОС 3: УТВЕРЖДЕНИЕ ПРО КЛЕММУ
        {
            "question": "3. Welche Behauptung ueber die gekennzeichneten Teile (Bild 10/2) des Messschiebers is richtig?",
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
        # ВОПРОС 4: ТЕМПЕРАТУРА LÄNGENPRÜFTECHNIK
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
        # ВОПРОС 5: ПОНЯТИЕ MESSEN
        {
            "question": "5. Wie kann the Begriff „Messen“ erklärt werden?",
            "type": "choice",
            "choices": [
                "a) Messen is das Ermitteln von Nennmaßen mit gesetzlich vorgeschriebenem Maßstab.",
                "b) Messen is das Ermitteln von absolut genauen Maßen.",
                "c) Messen is das Überprüfen einer Maßtoleranz mit einer Lehre.",
                "d) Messen is das Messen einer Länge oder eines Winkels mit einem Messgerät.",
                "e) Messen is das Vergleichen eines Prüfgegenstandes mit einer Lehre."
            ],
            "correct": [
                "d) Messen is das Messen einer Länge oder eines Winkels mit einem Messgerät."
            ]
        },
        # ВОПРОС 6: ПОНЯТИЕ LEHREN
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
        # ВОПРОС 7: ОШИБКИ ИЗМЕРЕНИЯ
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
        # ВОПРОС 8: НАПРАВЛЕНИЕ ВЗГЛЯДА
        {
            "question": "8. Beim Ablesen des Stahlmaßstabs muss zur Vermeidung von Parallaxe die Blickrichtung beachtet werden. Welche Blickrichtung ist richtig?",
            "type": "choice",
            "image": "blickrichtungen.jpeg",
            "choices": [
                "a) A",
                "b) B",
                "c) C",
                "d) D",
                "e) E"
            ],
            "correct": [
                "c) C"
            ]
        },
        # ВОПРОС 9: ВЫБОР ИЗМЕРИТЕЛЬНОЙ ОПЕРАЦИИ
        {
            "question": "9. Wie ist die Ausschussseite eines Grenzlehrdorns gekennzeichnet?",
            "type": "choice",
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
        # ВОПРОС 10: ПРОВЕРКА Grenzrachenlehre
        {
            "question": "10. Welche Behauptung über das Prüfen mit der Grenzrachenlehre ist richtig?",
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

# Логика перемешивания
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
    
    # Отображение локальной картинки
    if "image" in q:
        img_name = q["image"]
        # Проверяем, существует ли файл локально в папке приложения
        if os.path.exists(img_name):
            st.image(img_name, use_column_width=True)
        else:
            st.error(f"Datei '{img_name}' wurde im Projektordner nicht gefunden. Bitte lade sie hoch.")
    
    q_type = q.get("type", "choice")
    user_answers = {}

    if q_type == "text_input":
        st.write("Geben Sie die korrekten Bezeichnungen ein:")
        col1, col2 = st.columns(2)
        keys = list(q["inputs"].keys())
        
        for i, key in enumerate(keys):
            target_col = col1 if i < len(keys)/2 else col2
            with target_col:
                user_answers[key] = st.text_input(f"{key.upper()} =", key=f"text_{st.session_state.current_idx}_{key}").strip().lower()

    elif q_type == "unfall_inputs":
        st.caption("Пожалуйста, напишите 4 меры по технике безопасности ниже (любые 4 из 6 возможных вариантов):")
        with st.expander("Auswahloptionen (Доступные варианты для выбора)", expanded=True):
            for opt in q["hint_options"]:
                st.write(f"🔹 {opt}")
        
        user_answers["unfall_1"] = st.text_input("Maßnahme 1:", key=f"unf_{st.session_state.current_idx}_1").strip().lower()
        user_answers["unfall_2"] = st.text_input("Maßnahme 2:", key=f"unf_{st.session_state.current_idx}_2").strip().lower()
        user_answers["unfall_3"] = st.text_input("Maßnahme 3:", key=f"unf_{st.session_state.current_idx}_3").strip().lower()
        user_answers["unfall_4"] = st.text_input("Maßnahme 4:", key=f"unf_{st.session_state.current_idx}_4").strip().lower()
                
    else:
        st.caption("ℹ️ Eine Antwort auswählen:")
        selected_radio = st.radio("Optionen:", q["choices"], index=None, key=f"r_{st.session_state.current_idx}", label_visibility="collapsed")
        user_answers["choice"] = [selected_radio] if selected_radio else []

    if not st.session_state.answered:
        if st.button("Antworten", type="primary", use_container_width=True):
            empty = any(val == "" for val in user_answers.values()) if q_type in ["text_input", "unfall_inputs"] else not user_answers["choice"]
            if empty:
                st.warning("Bitte füllen Sie alle Felder aus / wählen Sie eine Antwort!")
            else:
                st.session_state.answered = True
                st.session_state.selected = user_answers
                st.rerun()
    else:
        if q_type == "text_input":
            all_correct = True
            st.write("### Ergebnisse der Überprüfung:")
            for key, accepted_answers in q["inputs"].items():
                user_val = st.session_state.selected.get(key, "")
                if user_val in accepted_answers:
                    st.success(f"✔️ **{key.upper()}**: {user_val.capitalize()}")
                else:
                    all_correct = False
                    st.error(f"❌ **{key.upper()}**: '{user_val}'. Erwartet: {accepted_answers[0].capitalize()}")
            
            if all_correct:
                st.success("🟢 Alle Antworten sind richtig!")
                if f"sc_{st.session_state.current_idx}" not in st.session_state:
                    st.session_state.score += 1
                    st.session_state[f"sc_{st.session_state.current_idx}"] = True

        elif q_type == "unfall_inputs":
            st.write("### Ergebnisse der Überprüfung:")
            entered_answers = [st.session_state.selected.get(f"unfall_{i}", "") for i in range(1, 5)]
            used_rule_indexes = set()
            correct_count = 0
            
            for idx, ans in enumerate(entered_answers, 1):
                matched = False
                for rule_idx, accepted_variants in enumerate(q["accepted_rules"]):
                    if ans in accepted_variants and rule_idx not in used_rule_indexes:
                        matched = True
                        used_rule_indexes.add(rule_idx)
                        break
                if matched:
                    st.success(f"✔️ **Maßnahme {idx}**: «{ans.capitalize()}»")
                    correct_count += 1
                else:
                    st.error(f"❌ **Maßnahme {idx}**: «{ans}» — Неверно или дубликат.")
            
            if correct_count == 4:
                st.success("🟢 Все 4 меры безопасности введены верно!")
                if f"sc_{st.session_state.current_idx}" not in st.session_state:
                    st.session_state.score += 1
                    st.session_state[f"sc_{st.session_state.current_idx}"] = True

        else:
            if set(st.session_state.selected.get("choice", [])) == set(q["correct"]):
                st.success("🟢 Richtig!")
                if f"sc_{st.session_state.current_idx}" not in st.session_state:
                    st.session_state.score += 1
                    st.session_state[f"sc_{st.session_state.current_idx}"] = True
            else:
                st.error("🔴 Falsch!")
                st.write("**Richtige Antwort:**")
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
