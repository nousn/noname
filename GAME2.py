import random

# Fungsi untuk cek jawaban fleksibel
def check_answer(user_answer, correct_answers):
    user_answer = user_answer.lower().strip()
    for ans in correct_answers:
        if ans.lower() in user_answer or user_answer in ans.lower():
            return True
    return False

# Fungsi untuk generate soal berdasarkan level
def generate_questions(level):
    base_questions = {
        "mudah": [
            {"q": "Apa ibu kota Indonesia?", "a": ["jakarta", "dki jakarta"], "p": 10},
            {"q": "Berapa jumlah planet di tata surya?", "a": ["8", "delapan"], "p": 15},
            {"q": "Apa warna langit pada siang hari?", "a": ["biru", "blue"], "p": 20},
            {"q": "Siapa presiden pertama Amerika Serikat?", "a": ["george washington", "washington"], "p": 25},
        ],
        "sedang": [
            {"q": "Apa sungai terpanjang di dunia?", "a": ["nil", "sungai nil", "nile"], "p": 30},
            {"q": "Berapa tahun dalam satu abad?", "a": ["100", "seratus", "seratus tahun"], "p": 35},
            {"q": "Apa unsur kimia dengan simbol O?", "a": ["oksigen", "oxygen"], "p": 40},
        ],
        "susah": [
            {"q": "Siapa penemu teori relativitas?", "a": ["einstein", "albert einstein"], "p": 50},
            {"q": "Apa nama benua terkecil?", "a": ["australia", "oceania"], "p": 55},
            {"q": "Berapa jumlah tulang dalam tubuh manusia dewasa?", "a": ["206", "dua ratus enam"], "p": 60},
        ],
    }
    # Tingkatkan kesulitan per level: tambah poin, ubah soal sedikit
    questions = {}
    for cat, qs in base_questions.items():
        questions[cat] = []
        for q in qs:
            new_q = q.copy()
            new_q["p"] += level * 5  # Poin naik per level
            # Ubah soal sedikit untuk variasi (contoh sederhana)
            if level > 1:
                new_q["q"] = new_q["q"].replace("Apa", f"Level {level}: Apa")
            questions[cat].append(new_q)
    return questions

# Fungsi utama game
def play_game():
    level = 1
    while True:
        print(f"\n=== Level {level} ===")
        questions = generate_questions(level)
        score = 0
        mistakes = {"mudah": 0, "sedang": 0, "susah": 0}
        max_mistakes = 1  # Maksimal salah 1 per kategori

        # Kategori mudah
        print("\n--- Kategori Mudah ---")
        for q in questions["mudah"]:
            print(q["q"])
            answer = input("Jawaban: ")
            if check_answer(answer, q["a"]):
                score += q["p"]
                print(f"Benar! +{q['p']} poin")
            else:
                mistakes["mudah"] += 1
                print("Salah!")
                if mistakes["mudah"] > max_mistakes:
                    print("Terlalu banyak salah di kategori mudah. Restart?")
                    if input("Ketik 'y' untuk restart, lainnya keluar: ").lower() == 'y':
                        return play_game()
                    else:
                        return

        # Kategori sedang
        print("\n--- Kategori Sedang ---")
        for q in questions["sedang"]:
            print(q["q"])
            answer = input("Jawaban: ")
            if check_answer(answer, q["a"]):
                score += q["p"]
                print(f"Benar! +{q['p']} poin")
            else:
                mistakes["sedang"] += 1
                print("Salah!")
                if mistakes["sedang"] > max_mistakes:
                    print("Terlalu banyak salah di kategori sedang. Restart?")
                    if input("Ketik 'y' untuk restart, lainnya keluar: ").lower() == 'y':
                        return play_game()
                    else:
                        return

        # Kategori susah
        print("\n--- Kategori Susah ---")
        for q in questions["susah"]:
            print(q["q"])
            answer = input("Jawaban: ")
            if check_answer(answer, q["a"]):
                score += q["p"]
                print(f"Benar! +{q['p']} poin")
            else:
                mistakes["susah"] += 1
                print("Salah!")
                if mistakes["susah"] > max_mistakes:
                    print("Terlalu banyak salah di kategori susah. Restart?")
                    if input("Ketik 'y' untuk restart, lainnya keluar: ").lower() == 'y':
                        return play_game()
                    else:
                        return

        # Akhir level
        print(f"\nTotal skor level {level}: {score}")
        choice = input("Pilih: 'next' untuk level berikutnya, 'restart' untuk mulai ulang: ").lower()
        if choice == 'next':
            level += 1
        elif choice == 'restart':
            level = 1
        else:
            break

# Jalankan game
play_game()
