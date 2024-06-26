// // ---------- NAMED PARAMETERS

// class Question {
//   late String questionText;
//   late bool questionAnswer;

//   Question({required String qT, required bool qA}) {
//     questionText = qT;
//     questionAnswer = qA;
//   }
// }

// // Question newQuestion = Question(qT: 'Is this real?', qA: true);

// ---------- POSITIONAL PARAMETERS

class Question {
  late String questionText;
  late bool questionAnswer;

  Question(String qT, bool qA) {
    questionText = qT;
    questionAnswer = qA;
  }
}

// Question newQuestion = Question('Is this real?', true);

// ------------------------------
