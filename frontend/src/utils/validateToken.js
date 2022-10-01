import FetchFunction from "@/utils"

async function validateToken(){
    let jwt_token = localStorage.getItem('jwt_token');
    console.log("token = "+jwt_token);
    if(jwt_token){
      let url = "http://localhost:5000/api/tokenValidation/get"
      let resp = await FetchFunction({url:url,authRequired:true}).then((d)=>{
        return true;
      }).catch((e)=>{
        return false;
      })
    }
    else{
      console.log("Returned false");
      return false
    }
  }
  
  export default validateToken