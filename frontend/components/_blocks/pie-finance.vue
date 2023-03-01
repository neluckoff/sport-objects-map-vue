<template>
    <section>
        <client-only>
            <pie-chartjs :chart-data="chartData" v-if="showGraph" />
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
            chartData: {}
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
                                    // label: 'Финансирование спортивного объекта',
                                    backgroundColor: [ '#1E9600', '#99C802', '#FFF200', '#F89403' ],
                                    data: response,
                                },
                            ]
                        }
                        this.showGraph = true;
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