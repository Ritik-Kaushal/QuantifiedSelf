<template>
  <div>
    <nav
      class="navbar navbar-expand-lg navbar-light"
      style="background-color: #b0d4ee"
    >
      <div class="container-fluid">
        <img
          src="@/assets/logo.jpg"
          alt=""
          width="30"
          height="25"
          class="d-inline-block align-text-top"
        />
        <div class="name">
          <strong>Track It</strong>
        </div>

        <button
          id="menu-id"
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul
            class="small-screen-nav nav-item-hover nav nav-pills navbar-nav me-auto mb-2 mb-lg-0"
          >
            <li class="nav-item ml-1 mx-1 nav-item-highlight">
              <router-link
                @click.native="reset"
                class="nav-link"
                aria-current="page"
                to="/home"
                >Home</router-link
              >
            </li>

            <li class="nav-item ml-1 mx-1 nav-item-highlight">
              <router-link
                @click.native="closeToggle"
                class="nav-link"
                aria-current="page"
                to="/faqs"
                >Faqs</router-link
              >
            </li>

            <li class="nav-item ml-1 mx-1 nav-item-highlight">
              <router-link
                @click.native="closeToggle"
                class="nav-link"
                aria-current="page"
                to="/acknowledgements"
                >Acknowledgements</router-link
              >
            </li>
          </ul>

          <div v-if="loggedIn">
            <div class="mx-2">
              <ul
                class="small-screen-nav nav-item-hover nav nav-pills navbar-nav me-auto mb-2 mb-lg-0"
              >
                <li
                  class="btn-outline-danger nav-item ml-1 mx-1 nav-button-highlight"
                >
                  <router-link
                    @click.native="closeToggle"
                    class="nav-link"
                    aria-current="page"
                    to="/dashboard"
                    >Go to Dashboard</router-link
                  >
                </li>
              </ul>
            </div>
          </div>
          <div v-else>
            <div class="mx-2">
              <ul
                class="small-screen-nav nav-item-hover nav nav-pills navbar-nav me-auto mb-2 mb-lg-0"
              >
                <li
                  class="btn-outline-danger nav-item ml-1 mx-1 nav-button-highlight"
                >
                  <router-link
                    @click.native="addClass"
                    class="nav-link"
                    aria-current="page"
                    to="/home/login"
                    >Login</router-link
                  >
                </li>

                <li
                  class="btn-outline-danger nav-item ml-1 mx-1 nav-button-highlight"
                >
                  <router-link
                    @click.native="addClass"
                    class="nav-link"
                    aria-current="page"
                    to="/home/register"
                    >Register</router-link
                  >
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import validateToken from "../utils/validateToken";
export default {
  name: "TopNavBar",
  mounted() {
    if(validateToken()){
      if (
        window.location.pathname === "/home/login" ||
        window.location.pathname === "/home/register"
      ) {
        this.addClass();
      }
    }
    else{
      this.$store.dispatch('logoutUser');
    }
    
  },
  data() {
    return {
      loggedIn: this.$store.state.user_store.loggedIn,
    };
  },
  methods: {
    closeToggle() {
      const element1 = document.getElementById("menu-id");
      element1.classList.add("collapsed");
      const element2 = document.getElementById("navbarSupportedContent");
      element2.classList.remove("show");
    },
    reset() {
      this.closeToggle();
      this.$store.dispatch("remClass");
    },
    addClass() {
      this.closeToggle();
      this.$store.dispatch("addClass");
    },
  },
};
</script>

<style scoped>
.name {
  font-size: 20px;
  font-family: "Courier New", Courier, monospace;
  padding-top: 5px;
  padding-left: 10px;
  padding-right: 10px;
}

.nav-item-highlight a.router-link-exact-active {
  background-color: blue;
}

.nav-item-highlight a.router-link-active {
  background-color: blue;
}

.nav-button-highlight {
  border: 1.5px solid #dc3545;
  border-radius: 8px;
}
.nav-button-highlight a.router-link-exact-active {
  background-color: #dc3545;
}

.button_login_logout_dashboard {
  color: black;
  text-decoration: none;
}

@media screen and (max-width: 990px) {
  .navbar-nav .nav-link {
    padding-right: 70px;
    padding-left: 70px;
  }

  .small-screen-nav {
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
