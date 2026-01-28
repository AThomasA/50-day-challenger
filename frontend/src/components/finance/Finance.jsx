import { useFinance } from "../../hooks/useFinance";
import SummaryForm from "./components/SummaryForm";
import RevenueForm from "./components/RevenueForm";
import ExpenseForm from "./components/ExpenseForm";

export default function Finance() {
  const { summary, loading } = useFinance();

  if (loading) return <p>Carregando...</p>;
  if (!summary) return null;

  return (
    <>
      <SummaryForm data={summary} />
      <RevenueForm />
      <ExpenseForm />
    </>
  );
}
