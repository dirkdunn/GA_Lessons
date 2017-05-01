import React, {Component} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import addUser from '../actions/addUser';

class AddUser extends Component {
  constructor(props){
    super(props)

    this.state = {
      first: '',
      last: '',
      description: ''
    }
  }

  render(){
    return(
      <form onSubmit={e => this.props.addUser(e,this.state.first,this.state.last,this.state.description)}>
        <input type="text" placeholder="firstname" value={this.state.first} onChange={e => this.setState({first: e.target.value})} />
        <input type="text" placeholder="lastname" value={this.state.last} onChange={e => this.setState({last: e.target.value})} />
        <input type="text" placeholder="description"value={this.state.description}  onChange={e => this.setState({description: e.target.value})}/>
        <input type="submit" value="add a user" />
      </form>
    )
  }
}

function mapStateToProps(state){
  return {
    state: state
  }
}

function mapDispatchToProps(dispatch){
  return bindActionCreators({ addUser },dispatch)
}

export default connect(mapStateToProps,mapDispatchToProps)(AddUser)
