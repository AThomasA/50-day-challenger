import { useFinance } from "../../hooks/useFinance";
import SummaryForm from "./components/SummaryCard";
import RevenueForm from "./components/RevenueForm";
import ExpenseForm from "./components/ExpenseForm";

export default function Finance() {
  const {
    summary,
    loading,
    startDate,
    endDate,
    setStartDate,
    setEndDate,
  } = useFinance();

  return (
    <>
      <h2>Finance</h2>

      {/* Filtro por período */}
      <div>
        <label>
          Data inicial:
          <input
            type="date"
            value={startDate || ""}
            onChange={(e) => setStartDate(e.target.value)}
          />
        </label>

        <label>
          Data final:
          <input
            type="date"
            value={endDate || ""}
            onChange={(e) => setEndDate(e.target.value)}
          />
        </label>
      </div>

      {loading && <p>Carregando...</p>}

      {summary && <SummaryCard data={summary} />}

      <RevenueForm />
      <ExpenseForm />
    </>
  );
}
