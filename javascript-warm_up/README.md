# JavaScript - Warm Up

## Description
This project is a first contact with **JavaScript** running on **Node.js**. Each script is a small command-line program covering the basics of the language: printing, reading command-line arguments, conditions, loops, functions, recursion, objects and CommonJS modules (`exports`).

## 📝 Learning Objectives
* Run JavaScript files with Node.js (`#!/usr/bin/node` shebang).
* Print to the console with `console.log` and template literals.
* Read command-line arguments with `process.argv`.
* Convert values with `Number.parseInt` and check for `NaN`.
* Use `if`/`else`, `for` / `for...of` loops, functions and recursion.
* Create and update objects, and add methods that use `this`.
* Export functions from a file with `exports` and pass functions as arguments (callbacks).

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `node` (Node.js)
* **Execution:** All scripts are executable (`chmod +x`) and start with `#!/usr/bin/node`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-javascript_is_amazing.js` | First constant | Prints `JavaScript is amazing` stored in a constant. |
| `1-multi_languages.js` | Multiple languages | Prints `C is fun`, `Python is cool`, `JavaScript is amazing`. |
| `2-arguments.js` | Arguments | Prints `No argument`, `Argument found` or `Arguments found` depending on the number of arguments. |
| `3-value_argument.js` | Value argument | Prints the first argument, or `No argument`. |
| `4-concat.js` | Concat | Prints `<arg1> is <arg2>`. |
| `5-to_integer.js` | Integer | Prints `My number: <n>` if the first argument is an integer, `Not a number` otherwise. |
| `6-multi_languages_loop.js` | Loop | Prints the three language lines from an array, using a loop. |
| `7-multi_c.js` | Multi occurrences | Prints `C is fun` as many times as the first argument (`Missing number of occurrences` if invalid). |
| `8-square.js` | Square | Prints a square of `X` characters whose size is the first argument (`Missing size` if invalid). |
| `9-add.js` | Add | Defines `add(a, b)` and prints the sum of the first two arguments. |
| `10-factorial.js` | Factorial | Prints the factorial of the first argument, computed recursively. |
| `11-second_biggest.js` | Second biggest | Prints the second biggest integer among the arguments (`0` if fewer than two). |
| `12-object.js` | Object | Prints an object, changes its `value` from 12 to 89, and prints it again. |
| `13-add.js` | Module | Exports an `add(a, b)` function. |
| `100-let_me_const.js` | Let it be a const | Variable assignment exercise: sets `myVar` to `333`. |
| `101-call_me_moby.js` | Call me Moby | Exports `callMeMoby(x, theFunction)`, which calls `theFunction` `x` times. |
| `102-add_me_maybe.js` | Add me maybe | Exports `addMeMaybe(number, theFunction)`, which calls `theFunction` with `number + 1`. |
| `103-object_fct.js` | Object function | Adds an `incr` method to an object that increments its `value`; calls it three times and prints the object after each call. |

---

## 🚀 Execution

```bash
chmod +x 4-concat.js
./4-concat.js Python "is cool"
```

```bash
node 9-add.js 3 5
```

Modules (`13-add.js`, `101-call_me_moby.js`, `102-add_me_maybe.js`) are meant to be imported:

```bash
node -e "console.log(require('./13-add.js').add(2, 3))"
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)
