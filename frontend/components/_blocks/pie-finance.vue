<template>
    <section>
        <client-only>
            <doughnut-chartjs :chart-data="chartData" :options="options" />
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
            items: [],
            chartData: {},
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        };
    },
    methods: {
		async fetch() {
            this.showGraph = false;
			try {
				if (!this.add) {
					let response = await this.$axios.$get(
						`/api/v1/financing/${this.idObject}`,
						{}
					);
					if (response) {
						this.chartData = {
                            labels: ['Федеральный бюджет', 'Бюджет субъекта федерации', 
                            'Бюджет муниципального образования', 'Внебюджетные источники' ],
                            datasets: [
                                {
                                    // label: 'Финансирование спортивного ~объекта',
                                    backgroundColor: [ '#03cf7a', '#d93d3d', '#fec94c', '#A3586D' ],
                                    data: response,
                                },
                            ]
                        }
					}
				}
			} catch (err) {
				console.log(err);
			}
		},
	},
    async mounted() {
        this.fetch()
    },
  }
</script>