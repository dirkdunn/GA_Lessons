/* action creator */

export default (user) => {
  console.log('user name is: ', user);

  /*action*/
  return {
    type: 'SELECT_USER',
    payload: user
  }
}
