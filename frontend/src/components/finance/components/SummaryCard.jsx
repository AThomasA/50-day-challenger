import Card from "../../ui/Card";
import { formatCurrency } from "../../../utils/formatters";

export default function SummaryCard({ data }) {
  return (
    <Card>
      <h2>Resumo</h2>

      <p>Total Receita: {formatCurrency(data.revenue.total)}</p>
      <p>Maior Receita: {formatCurrency(data.revenue.max)}</p>
      <p>Menor Receita: {formatCurrency(data.revenue.min)}</p>

      <hr />

      <p>Total Despesa: {formatCurrency(data.expense.total)}</p>
      <p>Maior Despesa: {formatCurrency(data.expense.max)}</p>
      <p>Menor Despesa: {formatCurrency(data.expense.min)}</p>

      <hr />

      <strong>Saldo: {formatCurrency(data.balance)}</strong>
    </Card>
  );
}
