import React, { Component } from 'react';
import AddTodo from './containers/AddTodo';
import TodoList from './containers/TodoList.js';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="container">
      <div className="row">
        <AddTodo />
      </div>
      <div className="row">
        <TodoList />
      </div>
      </div>
    );
  }
}

export default App;
