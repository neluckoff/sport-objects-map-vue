<template>
    <section>
        <client-only>
            <p>{{ this.chartData.datasets.data }}</p>
            <pie-chartjs :chart-data="chartData" v-if="showGraph" />
            <p>{{ this.chartData.datasets }}</p>
            <p>{{ this.items }}</p>
        </client-only>
    </section>
</template>

<script>
  export default {
    props: {
        idObject: {
            type: Number,
            default: null,
        },
    },
    data() {
      return {
        showGraph: false,
        items: [],
        chartData: {
            labels: ['sad', 'ds', 'sd', 'fff' ],
            datasets: [
                {
                    // label: 'Title',
                    backgroundColor: [ '#1E9600', '#99C802', '#FFF200', '#F89403' ],
                    data: this.items,
                },
            ]
        }
      };
    },
    methods: {
		async fetch() {
            this.showGraph = true;
			try {
				if (!this.add) {
					let response = await this.$axios.$get(
						`/api/v1/financing/${this.idObject}`,
						{}
					);
					if (response) {
						this.chartData.datasets.data = response;
                        // this.showGraph = true;
                        console.log(this.chartData.datasets.data);
					}
				}
			} catch (err) {
				console.log(err);
			}
		},
	},
    async mounted() {
        this.fetch()
    }
  }
</script>