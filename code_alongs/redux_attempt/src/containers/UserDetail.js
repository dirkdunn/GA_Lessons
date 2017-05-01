import React, {Component} from 'react';
import {connect} from 'react-redux';

class UserDetail extends Component {
  render(){
    console.log('userdetail this.props: ', this.props)
    return(
      <div>
        <h1>{this.props.user.first} {this.props.user.last}</h1>
        <p>{this.props.user.description}</p>
      </div>
    )
  }
}

function mapStateToProps(state){
  return {
    user: state.showuser
  }
}

export default connect(mapStateToProps)(UserDetail);
