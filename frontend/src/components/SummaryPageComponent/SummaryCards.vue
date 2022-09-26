<template>
  <div class="container-fluid">
    <div class="row mt-4">
      <!-- No of Trackers -->
      <div class="col-md-4 mb-3">
        <div
          class="card text-dark bg-info mb-3 h-100 text-center"
          style="max-width: 18rem"
        >
          <div class="card-header">
            <span class="fw-bold">No of trackers</span>
            <span class="float-end">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-app-indicator"
                viewBox="0 0 16 16"
              >
                <path
                  d="M5.5 2A3.5 3.5 0 0 0 2 5.5v5A3.5 3.5 0 0 0 5.5 14h5a3.5 3.5 0 0 0 3.5-3.5V8a.5.5 0 0 1 1 0v2.5a4.5 4.5 0 0 1-4.5 4.5h-5A4.5 4.5 0 0 1 1 10.5v-5A4.5 4.5 0 0 1 5.5 1H8a.5.5 0 0 1 0 1H5.5z"
                />
                <path d="M16 3a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
              </svg>
            </span>
          </div>
          <div class="card-body">
            <h5 class="card-body float-middle">
              {{ input_dict["tracker_count"] }}
            </h5>
          </div>
        </div>
      </div>
      <!-- No of Trackers -->

      <!-- No of times edited logs -->
      <div class="col-md-4 mb-3">
        <div
          class="card text-dark bg-info mb-3 h-100 text-center"
          style="max-width: 18rem"
        >
          <div class="card-header">
            <span class="fw-bold">No of times edited logs</span>
            <span class="float-end">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-clock"
                viewBox="0 0 16 16"
              >
                <path
                  d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"
                />
                <path
                  d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0z"
                />
              </svg>
            </span>
          </div>
          <div class="card-body">
            <h5 class="card-body float-middle">
              {{ input_dict["count_edited"] }}
            </h5>
          </div>
        </div>
      </div>
      <!-- No of times edited logs -->

      <!-- Last edited -->
      <div class="col-md-4 mb-3">
        <div
          class="card text-dark bg-info mb-3 h-100 text-center"
          style="max-width: 18rem"
        >
          <div class="card-header">
            <span class="fw-bold">Last edited</span>
            <span class="float-end">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-clock"
                viewBox="0 0 16 16"
              >
                <path
                  d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"
                />
                <path
                  d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0z"
                />
              </svg>
            </span>
          </div>
          <div class="card-body">
            <h5 class="card-title float-middle">
              <span class="fw-bold">Date :&nbsp;</span
              >{{ input_dict["last_edited_date"] }}
            </h5>
            <h5 class="card-title float-middle">
              <span class="fw-bold">Time :&nbsp;</span
              >{{ input_dict["last_edited_time"] }}
            </h5>
          </div>
        </div>
      </div>
      <!-- Last edited -->
    </div>
  </div>
</template>

<script>
    export default{
        name:'SummaryCards',
        props:['input_dict'],
    }
</script>

