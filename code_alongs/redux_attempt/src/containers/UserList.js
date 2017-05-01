import React, {Component} from 'react';
import { connect } from 'react-redux';
import {bindActionCreators} from 'redux';
import getUserDetails from '../actions/getUserDetails';
import AddUser from './AddUser';


class UserList extends Component {
  render(){
    const users = this.props.users.map(user => {
      // console.log('props: ', this.props)
      return(
        <li onClick={e => this.props.getUserDetails(user) } key={user.id}>{user.first} {user.last}</li>
      )
    });

    return (
      <div>
      <ul className="users">
      { users }
      </ul>
      <AddUser />
      </div>
    )
  }
}

function mapStateToProps(state){
  return {
    users: state.users
  }
}

/* add our action event handler in as props*/
function mapDispatchToProps(dispatch){
  return bindActionCreators({
    getUserDetails : getUserDetails
  },dispatch)
}

export default connect(mapStateToProps, mapDispatchToProps)(UserList);
