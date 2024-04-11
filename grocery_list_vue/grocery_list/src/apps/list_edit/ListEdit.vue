<template>
    <div>
        list edit.js should be here
    </div>
    
</template>


<script>
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'


export default {
    name: 'App',
    components: {
        VueDatePicker
    },
    data: function () {
        return {
            csrf_token: ext_csrf_token,
            form: ext_form,
            glist_dico: ext_glist_dict,
            date: this.init_date(ext_glist_dict.date_of_creation),
            grocery_list_source: ext_grocery_list,
            grocery_list : ext_glist_dict.groceries


        }
    },

    methods: {

    },
    computed: {
    }
}



</script>

