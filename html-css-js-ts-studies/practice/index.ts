export {}

// class Philosopher {
//     public first: string;
//     private last: string;
//     constructor(first: string, last: string) {
//         this.first = first;
//         this.last = last;
//     }
// }

// const philosopher1 = new Philosopher('Immanuel', 'Kant');

// class Philosopher {
//     constructor(
//         public first: string,
//         public last: string,
//         private _score: number
//     ) {}

//     get score(): number {
//         return this._score;
//     }

//     set score(newScore: number) {
//         if (newScore < 0) {
//             throw new Error('Score must be non-negative');
//         }
//         this._score = newScore;
//     }
        
//     get fullName(): string {
//         return `${this.first} ${this.last}`;
//     }
// }


// const philosopher1 = new Philosopher('Immanuel', 'Kant', 30);
// philosopher1.fullName; // Immanuel Kant
// philosopher1.score; // 30

// class Player {
//     first: string;
//     last: string;
//     score: number = 0; // another example
//     constructor(first: string, last: string) {
//         this.first = first;
//         this.last = last;
//     }
// }

// class SuperPlayer extends Player {
//     constructor(first: string, last: string) {  
//         super(first, last);
//     }
// }

class Person {
    constructor(
        private _id: number,
        public firstName: string,
        public lastName: string,
        public age: number
    ) {
        this._id = _id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }
}