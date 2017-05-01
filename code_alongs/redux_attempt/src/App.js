import React, { Component } from 'react';
import UserList from './containers/UserList';
import UserDetail from './containers/UserDetail';
import './App.css';

class App extends Component {
  render() {
    return (
      <div>
        <h2>User List</h2>
        <UserList />
        <hr />
        <h2>User Details</h2>
        <UserDetail />
      </div>
    );
  }
}

export default App;
