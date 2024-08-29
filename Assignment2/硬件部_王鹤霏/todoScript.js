function updateClock(){
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    const timeString = `${hours}:${minutes}:${seconds}`;
    document.getElementById('clock').textContent = timeString;
}
function addList(todoItem){
    var todoList = document.getElementById('list-todo');
    var doneList = document.getElementById('list-done');
    var todoItemElement = document.createElement('li');
    todoItemElement.className = 'display-board item';
    todoList.appendChild(todoItemElement);
    // item value
    var itemValue = document.createElement('span');
    itemValue.className = 'item-value';
    itemValue.textContent = todoItem;
    todoItemElement.appendChild(itemValue);
    // Edit button
    var editButton = document.createElement('button');
    var editBox = document.createElement('input');
    var editBoxSpan = document.createElement('span');
    editButton.textContent = 'Edit';
    editBoxSpan.appendChild(editBox);
    editBoxSpan.appendChild(editButton);
    editBox.type = 'text';
    editBox.placeholder = 'Edit item';
    todoItemElement.appendChild(editBoxSpan);
    editButton.addEventListener("click", function(){
        todoItemElement.getElementsByClassName("item-value")[0].textContent = editBox.value;
        editBox.value = '';
    });   
    // Done button
    var checkbox = document.createElement('button');
    checkbox.textContent = 'Done';
    todoItemElement.appendChild(checkbox);
    checkbox.addEventListener('click', function(){
        todoList.removeChild(todoItemElement);
        let doneItem = todoItemElement.getElementsByClassName("item-value")[0].textContent;
        let doneItemElement = document.createElement('li');
        doneItemElement.className = 'display-board item';
        doneItemElement.textContent = doneItem;
        doneList.appendChild(doneItemElement);
    });
    // Delete button
    var deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    todoItemElement.appendChild(deleteButton);
    deleteButton.addEventListener('click', function(){
        todoList.removeChild(todoItemElement);
    }); 
}
var todoList = [];
var todoInput = document.getElementById('input-todo');
const todoButton = document.getElementById('btn-add');
setInterval(updateClock, 1000);
todoButton.addEventListener('click', function(){
    var todo = todoInput.value;
    todoInput.value = '';
    todoList.push(todo);
    addList(todo);
});
console.log('todoScript.js loaded');