<template>
  <div class="register-part" ref="scroll">
    <div v-if="loading">
      <p class="register-part"><strong>Registering... Please  Wait</strong></p>
    </div>
    <div v-else>
      <form>
        <p class="register-header"><strong>Create an Account</strong></p>
        <div class="alert alert-danger error" role="alert" v-if="api_error">{{error_message}}</div>
        <div class="form-outline mb-4 input-part">
          <input
            type="text"
            class="form-control"
            placeholder="Name"
            v-model="name"
          />
          <span class="error" v-if="name_error">Name is required !!!</span>
        </div>
        <div class="form-outline mb-4 input-part">
          <input
            type="email"
            class="form-control"
            placeholder="Email address"
            v-model="email"
          />
          <span class="error" v-if="email_error">Email is required !!! </span>
        </div>
        <div class="form-outline mb-4 input-part">
          <input
            type="password"
            class="form-control"
            placeholder="Password"
            v-model="password"
          />
          <span class="error" v-if="password_error">Password cannot be empty !!! </span>
        </div>

        <div class="form-outline mb-4 input-part">
          <input
            type="password"
            class="form-control"
            placeholder="Re-enter Password"
            v-model="re_password"
          />
          <span class="error" v-if="re_password_error">Both the passwords must match !!!</span>
        </div>

        <div class="text-center pt-1 mb-5 pb-1">
          <button
            @click="register($event)"
            class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3"
            type="button"
            id="register_button"
          >
            Create Account
          </button>
          <br />
        </div>
        <div
          class="d-grid align-items-center justify-content-center pb-4"
          id="custom-create-part"
        >
          <p class="mb-0 me-2">Already have an account?</p>
          <button type="button" class="btn btn-outline-danger">
            <router-link @click.native="addClass" to="/home/login"
              >Login</router-link
            >
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import FetchFunction from "@/utils";
export default {
  name: "REGISTER",
  mounted() {
    if (this.$store.getters.get_login_status) {
      this.$router.push({ name: "Dashboard" });
    }
    this.$refs["scroll"].scrollIntoView();
  },
  data() {
    return {
      loading: false,
      api_error : false,
      error_message : "",
      email: "",
      email_error : false,
      password: "",
      password_error : false,
      re_password: "",
      re_password_error : false,
      name: "",
      name_error : false
    };
  },
  methods: {
    async register(e) {
      this.loading = true;
      e.preventDefault();
      const user = {
        email: this.email,
        password: this.password,
        password_confirm: this.re_password,
        name: this.name,
      };
      const res = await FetchFunction({
        url: "http://127.0.0.1:5000/api/register",
        init_obj: {
          headers: {
            "Content-Type": "application/json",
          },
          method: "POST",
          body: JSON.stringify(user),
        },
      })
        .then(async (data) => {
          const user_conf = { email: this.email };
          const res = await FetchFunction({
            url: "http://127.0.0.1:5000/confirm",
            init_obj: {
              headers: {
                "Content-Type": "application/json",
              },
              method: "POST",
              body: JSON.stringify(user_conf),
            },
          })
            .then((data) => {
              alert(
                "Please check your email. A confirmation link has been sent."
              );
              this.loading = false;
              this.$router.push({ path: "/home/login" });
            })
            .catch((err) => {
              console.log(err);
            });
        })
        .catch((err) => {
          this.loading = false;
          err = JSON.parse(err.message);
          this.error_message = err.response.field_errors.email[0]
          this.api_error = true
        });
    },
  },
  watch : {
    name(){
      if(this.name.trim() == ""){
        this.name_error = true
        document.getElementById("register_button").disabled = true;

      }
      else{
        this.name_error = false
        document.getElementById("register_button").disabled = false;
      }
    },
    email(){
      if(this.email.trim() == ""){
        this.email_error = true
        document.getElementById("register_button").disabled = true;

      }
      else{
        this.email_error = false
        document.getElementById("register_button").disabled = false;
      }
    },
    password(){
      if(this.password.trim() == ""){
        this.password_error = true
        document.getElementById("register_button").disabled = true;

      }
      else{
        this.password_error = false
        document.getElementById("register_button").disabled = false;
      }
    },
   re_password(){
      if(this.re_password.trim() == "" || this.re_password != this.password){
        this.re_password_error = true
        document.getElementById("register_button").disabled = true;

      }
      else{
        this.re_password_error = false
        document.getElementById("register_button").disabled = false;
      }
    }
  }
};
</script>

<style scoped>
.register-part {
  display: grid;
  position: relative;

  justify-content: center;
  align-items: center;
}
.register-part {
  display: grid;
}
.register-header {
  margin-top: 2rem;
  font-weight: 500;
  margin: 2rem auto;
  text-align: center;
}
a {
  text-decoration: none;
  color: black;
}
.error{
  display: flex;
  position: relative;
  color : red
}

</style>
