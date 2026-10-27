# JavaScript - DOM Manipulation

## Description
This project covers manipulating a web page from JavaScript in the browser: selecting elements, changing styles and content, reacting to events, creating and removing nodes, and fetching data from remote APIs with `fetch`. Each task is a pair made of an HTML page (`indexN.html`) and the script it loads (`N-script.js`).

## 📝 Learning Objectives
* Select elements with `document.querySelector`.
* Change styles, classes (`classList.add/remove/contains`) and text (`textContent`).
* React to user actions with `addEventListener` (`click`, `DOMContentLoaded`).
* Create, append and remove DOM nodes (`createElement`, `appendChild`, `removeChild`).
* Fetch JSON from an API with `fetch(...).then(...)` and display it in the page.
* Read the value of a form control (`<select>`) and use it in a request.

## 🛠️ Requirements & Engineering Constraints
* **Environment:** A modern web browser (scripts run in the page, not in Node.js).
* **APIs used:** [SWAPI mirror](https://swapi-api.hbtn.io/) and [HelloSalut](https://hellosalut.stefanbohacek.com/).
* **Layout:** Each `indexN.html` loads its `N-script.js` through a `<script>` tag.

## 📁 File List & Tasks Directory

| Files | Task Title | Description |
| :--- | :--- | :--- |
| `0-script.js`, `index0.html` | Change header color | Sets the `<header>` text color to `#FF0000`. |
| `1-script.js`, `index1.html` | Click and turn red | Turns the `#red_header` element red when clicked. |
| `2-script.js`, `index2.html` | Add `.red` class | Adds the `red` class to the `<header>` when `#red_header` is clicked. |
| `3-script.js`, `index3.html` | Toggle classes | Switches the `<header>` between the `red` and `green` classes when `#toggle_header` is clicked. |
| `4-script.js`, `index4.html` | List of items | Appends a new `<li>Item</li>` to `.my_list` when `#add_item` is clicked. |
| `5-script.js`, `index5.html` | Update the text | Replaces the `<header>` text with `New Header!!!` when `#update_header` is clicked. |
| `6-script.js`, `index6.html` | Star Wars character | Fetches character #5 from the SWAPI mirror and shows its name in `#character`. |
| `7-script.js`, `index7.html` | Star Wars movies | Fetches the list of films and appends each title as a `<li>` in `#list_movies`. |
| `8-script.js`, `index8.html` | Hello in French | Once the DOM is loaded, fetches the French greeting and displays it in `#hello`. |
| `100-script.js`, `index100.html` | Add, remove and clear | Buttons to add an item, remove the last item, or clear the whole `.my_list`. |
| `101-script.js`, `index101.html` | Translate | Fetches the greeting for the language chosen in the `<select>` and displays it in `#hello` when `#btn_translate` is clicked. |

---

## 🚀 Execution

Open a page directly in a browser:

```bash
xdg-open index0.html
```

Or serve the folder locally (some browsers restrict `fetch` on `file://` pages):

```bash
python3 -m http.server 8000
# then browse to http://localhost:8000/index6.html
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)
