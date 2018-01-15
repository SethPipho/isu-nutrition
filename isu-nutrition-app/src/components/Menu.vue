<template>
    <div>
    <br>
       <h3> {{diningCenterName}} </h3>

        <select v-model="selectedMeal" class="form-control">
            <option value="all">All </option>
            <option  v-for="(mealData,mealName) in menu" :value="mealName">{{mealName}}</option> 
        </select>
        <br>
        
        <div  v-for="(stationData, stationName) in menu[selectedMeal]">
            <h5> {{ stationName }} </h5>
           
           
            <table class="table">
           
            <tbody>
                <tr  v-for="food in stationData">
                    <td> <b> {{food.name}} </b> <br> ({{food.servingSize}})</td>
                    <td class='macros'>
                    <span> <b> {{food.calories}} </b> </span>
                    | <span style="color:red">{{formatMacros(food['fat'])}} </span>
                    | <span style="color:green">{{formatMacros(food['carbs'])}} </span>
                    | <span style="color:blue">{{formatMacros(food['protein'])}} </span>
                    
                    </td>
                   
                  
                </tr>
            </tbody>
            </table>
            
                
        </div> 
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data(){
            return{
               diningCenterName:'',
               menu: {},
               selectedMeal:''
            }
        },
        methods: {
            formatMacros:function(str){
                return isNaN(parseInt(str)) ? "<1":parseInt(str);
            },
            update() {
                this.diningCenterName = this.$route.params.diningCenterName

                var monthNames = ["January", "February", "March", "April", "May", "June",
                                    "July", "August", "September", "October", "November", "December"
                ];

                let date = new Date();
                let dateString = monthNames[date.getMonth()] + '_' + date.getDate() + '_' + date.getFullYear()
                console.log(dateString)

                let url = 'https://sethpipho.github.io/isu-nutrition-data/data/' + this.diningCenterName.split(' ').join('_') + '/' + dateString + '.json' 

                console.log(url)

                axios.get(url)
                    .then(respone => {
                        this.menu = respone.data
                        this.selectedMeal = Object.keys(this.menu)[0]
                    })
                
            }
        },
         watch: {
            '$route' (to, from) {
                this.update()  
            }
        },
        mounted(){
            this.update()
        }
          
    }
</script>
<style>

    .food-row {
        border-bottom: 1px solid black;
    }

    .macros {
        text-align:right;
        min-width:10em;
    }

</style>