<script>
import ExportModal from "./modals/exportModal.vue";
export default {
  name: "DashboardNavBar",
  components: {
    ExportModal,
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
