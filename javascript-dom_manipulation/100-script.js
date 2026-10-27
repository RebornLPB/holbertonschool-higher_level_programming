document.addEventListener('DOMContentLoaded', function () {
  const my_list = document.querySelector('.my_list');
  const add_item = document.querySelector('#add_item');
  const remove_item = document.querySelector('#remove_item');
  const clear_list = document.querySelector('#clear_list');

  add_item.addEventListener('click', function () {
    const new_item = document.createElement('li');
    new_item.textContent = 'Item';
    my_list.appendChild(new_item);
  });

  remove_item.addEventListener('click', function () {
    if (my_list.lastElementChild) {
      my_list.removeChild(my_list.lastElementChild);
    }
  });

  clear_list.addEventListener('click', function () {
    my_list.innerHTML = '';
  });
});
