<template>
  <div>
    <!-- Nav Bar-->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid">
        <!-- offcanvas trigger -->
        <button
          class="btn btn-primary navbar-toggler me-2"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasExample"
          aria-controls="offcanvasExample"
        >
          <span data-bs-target="#offcanvasExample">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-arrow-right"
              viewBox="0 0 16 16"
            >
              <path
                fill-rule="evenodd"
                d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"
              />
            </svg>
          </span>
        </button>
        <!-- offcanvas trigger -->

        <router-link class="navbar-brand fw-bold text-uppercase me-auto" to="/"
          >Track It</router-link
        >
      </div>
    </nav>
    <!-- Nav Bar-->

    <!-- Off Canvas -->
    <div
      class="offcanvas offcanvas-start sidebar-nav bg-dark text-white"
      tabindex="-1"
      id="offcanvasExample"
      aria-labelledby="offcanvasExampleLabel"
    >
      <div class="offcanvas-body p-7">
        <nav class="navbar-dark">
          <ul class="navbar-nav">
            <li>
              <div class="text-muted small fw-bold text-uppercase px-3 pt-2">
                CORE
              </div>
            </li>
            <li>
              <router-link to="/" class="nav-link px-3">
                <span class="me-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-house-door-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5z"
                    />
                  </svg>
                </span>
                <span>Go Home</span>
              </router-link>
            </li>
            <li>
              <router-link
                to="/dashboard/summary"
                class="nav-link px-3"
                v-bind:class="{
                  active: this.$store.state.summary_store.active_id[0],
                }"
              >
                <span class="me-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-speedometer"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M8 2a.5.5 0 0 1 .5.5V4a.5.5 0 0 1-1 0V2.5A.5.5 0 0 1 8 2zM3.732 3.732a.5.5 0 0 1 .707 0l.915.914a.5.5 0 1 1-.708.708l-.914-.915a.5.5 0 0 1 0-.707zM2 8a.5.5 0 0 1 .5-.5h1.586a.5.5 0 0 1 0 1H2.5A.5.5 0 0 1 2 8zm9.5 0a.5.5 0 0 1 .5-.5h1.5a.5.5 0 0 1 0 1H12a.5.5 0 0 1-.5-.5zm.754-4.246a.389.389 0 0 0-.527-.02L7.547 7.31A.91.91 0 1 0 8.85 8.569l3.434-4.297a.389.389 0 0 0-.029-.518z"
                    />
                    <path
                      fill-rule="evenodd"
                      d="M6.664 15.889A8 8 0 1 1 9.336.11a8 8 0 0 1-2.672 15.78zm-4.665-4.283A11.945 11.945 0 0 1 8 10c2.186 0 4.236.585 6.001 1.606a7 7 0 1 0-12.002 0z"
                    />
                  </svg>
                </span>
                <span>Dashboard</span>
              </router-link>
            </li>

            <li class="my-4">
              <hr class="dropdown-divider" />
            </li>

            <li>
              <div class="text-muted small fw-bold text-uppercase px-3">
                Tracker and Logs
              </div>
            </li>
            <li>
              <router-link
                to="/dashboard/trackers"
                class="nav-link px-3"
                v-bind:class="{
                  active: this.$store.state.summary_store.active_id[1],
                }"
              >
                <span class="me-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-columns-gap"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M6 1v3H1V1h5zM1 0a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H1zm14 12v3h-5v-3h5zm-5-1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1h-5zM6 8v7H1V8h5zM1 7a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H1zm14-6v7h-5V1h5zm-5-1a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1h-5z"
                    />
                  </svg>
                </span>
                <span>View Trackers</span>
              </router-link>
            </li>
            <li>
              <router-link
                to="/dashboard/trackersLogs"
                class="nav-link px-3"
                v-bind:class="{
                  active: this.$store.state.summary_store.active_id[2],
                }"
                ><span class="me-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-activity"
                    viewBox="0 0 16 16"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M6 2a.5.5 0 0 1 .47.33L10 12.036l1.53-4.208A.5.5 0 0 1 12 7.5h3.5a.5.5 0 0 1 0 1h-3.15l-1.88 5.17a.5.5 0 0 1-.94 0L6 3.964 4.47 8.171A.5.5 0 0 1 4 8.5H.5a.5.5 0 0 1 0-1h3.15l1.88-5.17A.5.5 0 0 1 6 2Z"
                    />
                  </svg>
                </span>
                <span>View Logs</span></router-link
              >
            </li>

            <li class="my-4">
              <hr class="dropdown-divider" />
            </li>

            <li>
              <div class="text-muted small fw-bold text-uppercase px-3">
                Import/Export
              </div>
            </li>

            <li>
              <router-link
                to="#"
                @click.native="Export($event)"
                class="nav-link px-3"
                type="button"
                id="export_nav"
                v-bind:class="{
                  active: this.$store.state.summary_store.active_id[3],
                }"
                ><span class="me-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-box-arrow-in-right"
                    viewBox="0 0 16 16"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M6 3.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 0-1 0v2A1.5 1.5 0 0 0 6.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-8A1.5 1.5 0 0 0 5 3.5v2a.5.5 0 0 0 1 0v-2z"
                    />
                    <path
                      fill-rule="evenodd"
                      d="M11.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H1.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"
                    />
                  </svg>
                </span>
                <span>Export your data</span></router-link
              >
            </li>

            <li class="my-4">
              <hr class="dropdown-divider" />
            </li>

            <li>
              <div class="text-muted small fw-bold text-uppercase px-3">
                Settings
              </div>
            </li>
            <li>
              <router-link
                to="/logout"
                class="nav-link px-3"
                v-bind:class="{
                  active: this.$store.state.summary_store.active_id[4],
                }"
                ><span class="me-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-power"
                    viewBox="0 0 16 16"
                  >
                    <path d="M7.5 1v7h1V1h-1z" />
                    <path
                      d="M3 8.812a4.999 4.999 0 0 1 2.578-4.375l-.485-.874A6 6 0 1 0 11 3.616l-.501.865A5 5 0 1 1 3 8.812z"
                    />
                  </svg>
                </span>
                <span>Logout</span></router-link
              >
            </li>
          </ul>
        </nav>
        <!-- Toast -->
        <div class="position-fixed top-0 end-0 p-3" style="z-index: 11">
          <div class="toast-container">
            <div
              class="toast"
              role="alert"
              aria-live="assertive"
              aria-atomic="true"
            >
              <div class="toast-header bg-warning">
                <strong class="me-auto">{{ toast_message }}</strong>
                <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="toast"
                  aria-label="Close"
                ></button>
              </div>
            </div>
          </div>
        </div>
        <!-- Toast -->
      </div>
    </div>
    <!-- Off Canvas -->
  </div>
</template>

<script>
import FetchFunction from "@/utils";
export default {
  name: "DashboardNavBar",
  data() {
    return {
      export_disabled: false,
      toast_message: "",
    };
  },
  methods: {
    async Export(e) {
      e.preventDefault();
      if (!this.export_disabled) {
        this.toast_message =
          "Exporting your data. Please  wait... You will be alerted once it is done.";
        $(".toast").toast("show");
        this.export_disabled = true;
        let url = "http://localhost:5000/api/exportData";
        let res = FetchFunction({
          url: url,
          authRequired: true,
        })
          .then((d) => {
            this.toast_message = d.message;
            this.export_disabled = false;
            $(".toast").toast("show");
          })
          .catch((e) => {
            const err = JSON.parse(e.message);
            this.toast_message = err.message;
            this.export_disabled = false;
            $(".toast").toast("show");

            if (err.error_code == "TIM" || err.error_code == "IVT") {
              this.$store.dispatch("logoutUser");
            }
          })
          .catch((e) => {
            this.toast_message = "Something went wrong. Please try again";
            this.export_disabled = false;
            $(".toast").toast("show");
          });
      }
    },
  },
};
</script>

<style scoped>
:root {
  --offcanvas-width: 270px;
  --topNavbarHeight: 56px;
}

.sidebar-nav {
  width: var(--offcanvas-width);
}

@media (min-width: 800px) {
  body {
    overflow: auto !important;
  }
  .offcanvas-backdrop::before {
    display: none;
  }

  .sidebar-nav {
    transform: none;
    visibility: visible !important;
    top: 56px;
    width: 270px;
  }
}
</style>
