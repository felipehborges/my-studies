// // ********** CLASSES, CONSTRUCTORS, SUPER() **********

// class Player {
//     constructor(firstName, lastName) {
//         this.firstName = firstName;
//         this.lastName = lastName;
//     }
// }

// const commonPlayer = new Player('Albert', 'Einstein');
// console.log(commonPlayer)

// class AdminPlayer extends Player {
//     constructor(firstName, lastName, powers) {
//         super(firstName, lastName);
//         this.powers = powers;
//     }
//     isAdmin = true
// }

// const admPlayer = new AdminPlayer('Leôncio', 'Silva', ['create', 'delete', 'update']);
// console.log(admPlayer)

// class SuperAdminPlayer extends AdminPlayer {
//     constructor(superPowers) {
//         super();
//         this.superPowers = superPowers;
//         this.powers = ['normalPowers', 'xablimba'];
//         this.firstName = 'Zeus';
//         this.lastName = 'God';
//     }
//     greetings() {
//         return `Hello, ${this.firstName} ${this.lastName}!`
//     }
// }

// const superAdmPlayer = new SuperAdminPlayer(['destroy', 'createLife']);
// console.log(superAdmPlayer)
