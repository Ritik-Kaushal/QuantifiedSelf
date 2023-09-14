<template>
  <div class="login-part" ref="scroll">
    <div v-if="loading">
      <p class="login-part"><strong>Logging In... Please Wait</strong></p>
    </div>
    <div v-else>
      <form>
        <p class="login-header"><strong>Login to your account</strong></p>
        <div class="alert alert-danger error" role="alert" v-if="api_error">
          {{ error_message }}
        </div>
        <div class="form-outline mb-4 input-part">
          <input type="email" class="form-control" placeholder="Email address" v-model="email" />
          <div class="error" v-if="email_error">Email is required !!!</div>
        </div>

        <div class="form-outline mb-4 input-part">
          <input type="password" class="form-control" placeholder="Password" v-model="password" />
          <div class="error" v-if="password_error">Password cannot be empty !!!</div>
        </div>

        <div class="text-center pt-1 mb-5 pb-1">
          <button @click="login($event)" class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="button"
            id="login_button">
            Log in
          </button>
          <br />
          <router-link to="/home/reset">Forgot Password ?
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import FetchFunction from "@/utils";
export default {
  name: "LOGIN",
  mounted() {
    if (this.$store.getters.get_login_status) {
      this.$router.push({ name: "Dashboard" });
    }
    this.$refs["scroll"].scrollIntoView();
  },
  data() {
    return {
      loading: false,
      email_error: false,
      password_error: false,
      api_error: false,
      error_message: "",
      email: "",
      password: "",
    };
  },
  methods: {
    async login(e) {
      this.loading = true;
      e.preventDefault();
      const user = { email: this.email, password: this.password };
      const res = await FetchFunction({
        url: "http://127.0.0.1:5000/api/login",
        init_obj: {
          headers: {
            "Content-Type": "application/json",
          },
          method: "POST",
          body: JSON.stringify(user),
        },
      })
        .then((data) => {
          const jwt_token = data["jwt_token"];
          localStorage.setItem("jwt_token", jwt_token);
          this.$store.commit("login");
          this.loading = false;
          this.$router.push({ name: "Dashboard" });
        })
        .catch((err) => {
          err = JSON.parse(err.message);
          this.error_message = err.error_message;
          this.api_error = true;
          this.loading = false;
        })
        .catch((e) => {
          this.error_message = "Something went wrong.";
          this.api_error = true;
          this.loading = false;
        });
    },
  },
  watch: {
    email() {
      if (this.email.trim() == "") {
        this.email_error = true;
        document.getElementById("login_button").disabled = true;
      } else {
        this.email_error = false;
        document.getElementById("login_button").disabled = false;
      }
    },
    password() {
      if (this.password.trim() == "") {
        this.password_error = true;
        document.getElementById("login_button").disabled = true;
      } else {
        this.password_error = false;
        document.getElementById("login_button").disabled = false;
      }
    },
  },
};
</script>

<style scoped>
.login-part {
  display: grid;
  position: relative;

  justify-content: center;
  align-items: center;
}

.input-part {
  display: grid;
}

.login-header {
  margin-top: 2rem;
  font-weight: 500;
  margin: 2rem auto;
  text-align: center;
}

a {
  text-decoration: none;
  color: black;
}

.error {
  align-items: center;
  justify-content: center;
  width: 100%;
  color: red;
}

.alert {
  padding-top: 4px;
  padding-bottom: 4px;
}
</style>
