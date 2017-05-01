import {combineReducers} from 'redux';
import UserReducer from './user_reducer';
import ShowUserReducer from './showuser_reducer';

const rootReducer = combineReducers({
  users: UserReducer,
  showuser: ShowUserReducer
});

export default rootReducer;
