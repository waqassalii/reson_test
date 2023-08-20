/* @odoo-module */
import { StockReportSearchPanel } from '@stock/views/search/stock_report_search_panel';
import { StockReportListView } from '@stock/views/list/stock_report_list_view';
export class StockReportSearchPanelExt extends StockReportSearchPanel {
    setup() {
        super.setup(...arguments);
    }
    submit_stock_report(){
        console.log('hello');
        var context = {'default_detailed_type': 'product'}
        context['from_date'] = $('#fromDate').val()
        context['to_date'] = $('#toDate').val()
        this.env.services['action'].doAction('stock.action_product_stock_view', {
            additionalContext: context,
            clearBreadcrumbs: false,
        });
    }
}
StockReportListView.SearchPanel = StockReportSearchPanelExt