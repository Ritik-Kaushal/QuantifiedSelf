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

        <a class="navbar-brand fw-bold text-uppercase me-auto" href="/"
          >Track It</a
        >
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto my-2 my-lg-0">
            <div class="dropdown">
              <a
                class="btn btn-secondary dropdown-toggle"
                href="#"
                role="button"
                id="dropdownMenuLink"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-person-circle"
                  viewBox="0 0 16 16"
                >
                  <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
                  <path
                    fill-rule="evenodd"
                    d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"
                  />
                </svg>
              </a>

              <ul
                class="dropdown-menu dropdown-menu-end"
                aria-labelledby="dropdownMenuLink"
              >
                <li>
                  <a class="dropdown-item" href="/edit_profile">Edit Profile</a>
                </li>
                <li><a class="dropdown-item" href="/logout">Logout</a></li>
              </ul>
            </div>
          </ul>
        </div>
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
              <a href="/" class="nav-link px-3">
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
              </a>
            </li>
            <li>
              <router-link
                to="/dashboard/summary"
                class="nav-link px-3"
                v-bind:class="{ active: this.$store.state.active_id[0] }"
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
                v-bind:class="{ active: this.$store.state.active_id[1] }"
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
                v-bind:class="{ active: this.$store.state.active_id[2] }"
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
          </ul>
        </nav>
      </div>
    </div>
    <!-- Off Canvas -->
  </div>
</template>

<script>
export default {
  name: "DashboardNavBar",
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
