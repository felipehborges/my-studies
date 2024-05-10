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

// class Player {
//     protected _score: number;
//     constructor(
//         private _id: number,
//         public firstName: string,
//         public lastName: string,
//         public age: number
//     ) {}
// }

// class SuperPlayer extends Player {
//     public isAdmin: boolean = true;
//     score = this._score;
// }

// // ***************** Implementing Interfaces *****************

// interface Colorful {
//     color: string;
// }

// interface Premium {
//     isPremium: boolean;
// }

// interface Printable {
//     print(): void;
// }

// class Shirt implements Colorful {
//     color: string;
// }

// class Jacket implements Colorful, Premium, Printable {
//     color: string;
//     isPremium: boolean;

//     print() {
//         console.log('This is a jacket');
//     }
// }

// abstract class Employee {
//     constructor(
//         public firstName: string, public lastName: string
//     ) {}
//     greet() {
//         console.log('Hi')
//     }
//     abstract getPay(): number;
// }

// class FullTimeEmployee extends Employee {
//     constructor(
//         firstName: string, lastName: string, private salary: number
//     ) {
//         super(firstName, lastName);
//     }
//     getPay(): number {
//         return this.salary;
//     }
// }

// class PartTimeEmployee extends Employee {
//     constructor(
//         firstName: string, lastName: string, private hourlyRate: number, private hoursWorked: number
//     ) {
//         super(firstName, lastName);
//     }

//     getPay(): number {
//         return this.hourlyRate * this.hoursWorked;
//     }
// }

// const betty = new FullTimeEmployee('Betty', 'Sue', 50000);
// const john = new PartTimeEmployee('John', 'Doe', 30, 20);

// // ***************** Generics *****************

// const numberIndentity = (item: number): number => {
//     return item;
// }
// const stringIdentity = (item: string): string => {
//     return item;
// }
// const booleanIdentity = (item: boolean): boolean => {
//     return item;
// }

// interface Employee {
//     name: string;
//     age: number;
//     isAllowed: boolean;
// }

// const identity = <T>(item: T): T => {
//     return item;
// }

// identity<number>(1);
// // const identity: <number>(item: number) => number
// identity<string>('Hello');
// // const identity: <string>(item: string) => string
// identity<boolean>(true);
// // const identity: <boolean>(item: boolean) => boolean

// identity('xablau');
// // const identity: <"xablau">(item: "xablau") => "xablau"

// identity<Employee>({ name: 'John', age: 30, isAllowed: true });
// // const identity: <Employee>(item: Employee) => Employee

function getRandomElement<T>(list: Array<T>): T {
    const randIdx = Math.floor(Math.random() * list.length);
    return list[randIdx];
}

getRandomElement<string>(['a', 'b', 'c']);
getRandomElement<number>([1, 2, 3]);
getRandomElement<boolean>([true, false]);
