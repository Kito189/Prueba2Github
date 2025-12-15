import { useState } from "react";
import Login from "./components/Login";
import Menu from "./components/Menu";
import Ordenes from "./components/Ordenes";
import Facturas from "./components/Facturas";
import Envios from "./components/Envios";

function App() {
  const [autenticado, setAutenticado] = useState(false);
  const [vista, setVista] = useState("ordenes");

  if (!autenticado) {
    return <Login onLogin={() => setAutenticado(true)} />;
  }

  return (
    <div className="min-vh-100 bg-light">
      <div className="container py-4">
        <div className="card shadow-sm">
          <div className="card-body">
            <h1 className="h3 text-center mb-4">Sistema de Gestión</h1>
            <Menu vista={vista} setVista={setVista} />

            <div className="mt-4">
              {vista === "ordenes" && <Ordenes />}
              {vista === "facturas" && <Facturas />}
              {vista === "envios" && <Envios />}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
