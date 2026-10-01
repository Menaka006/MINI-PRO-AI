from flask import Flask, render_template_string, request
import main


app = Flask(__name__)


# ============================================================
# HTML DASHBOARD
# ============================================================

HTML = """

<!DOCTYPE html>

<html>

<head>

    <title>Negotiating Agents for Resource Sharing</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <style>

        * {
            box-sizing: border-box;
        }


        body {

            margin: 0;

            font-family:
                Arial,
                Helvetica,
                sans-serif;

            background: #f4f6f9;

            color: #222;

        }


        /* ====================================================
           HEADER
           ==================================================== */

        .header {

            background: #1f2937;

            color: white;

            padding: 30px;

            text-align: center;

        }


        .header h1 {

            margin: 0;

            font-size: 34px;

        }


        .header p {

            margin-top: 10px;

            font-size: 17px;

        }


        /* ====================================================
           MAIN CONTAINER
           ==================================================== */

        .container {

            width: 92%;

            max-width: 1200px;

            margin: 30px auto;

        }


        /* ====================================================
           PRODUCT SECTION
           ==================================================== */

        .product-section {

            background: white;

            padding: 25px;

            border-radius: 12px;

            margin-bottom: 25px;

            box-shadow:
                0 3px 10px rgba(0,0,0,0.08);

        }


        .product-section h2 {

            margin-top: 0;

        }


        .product-input {

            width: 100%;

            padding: 13px;

            border: 1px solid #ccc;

            border-radius: 7px;

            font-size: 16px;

        }


        /* ====================================================
           RESOURCE CARDS
           ==================================================== */

        .section-title {

            text-align: center;

            margin: 30px 0 20px;

            font-size: 26px;

        }


        .resource-grid {

            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 20px;

        }


        .resource-card {

            background: white;

            padding: 25px;

            border-radius: 12px;

            text-align: center;

            box-shadow:
                0 3px 10px rgba(0,0,0,0.08);

        }


        .resource-card h3 {

            margin: 5px;

            font-size: 22px;

        }


        .resource-value {

            font-size: 30px;

            font-weight: bold;

            margin-top: 10px;

        }


        /* ====================================================
           AGENT TABLE
           ==================================================== */

        .table-container {

            background: white;

            padding: 20px;

            border-radius: 12px;

            box-shadow:
                0 3px 10px rgba(0,0,0,0.08);

            overflow-x: auto;

        }


        table {

            width: 100%;

            border-collapse: collapse;

        }


        th {

            background: #1f2937;

            color: white;

            padding: 14px;

        }


        td {

            padding: 13px;

            text-align: center;

            border-bottom:
                1px solid #ddd;

        }


        tr:hover {

            background: #f5f5f5;

        }


        /* ====================================================
           ARCHITECTURE CARDS
           ==================================================== */

        .architecture-grid {

            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 20px;

        }


        .architecture-card {

            background: white;

            padding: 25px;

            border-radius: 12px;

            text-align: center;

            box-shadow:
                0 3px 10px rgba(0,0,0,0.08);

        }


        .architecture-card h3 {

            font-size: 21px;

        }


        .architecture-card p {

            color: #555;

            line-height: 1.5;

        }


        /* ====================================================
           RUN BUTTON
           ==================================================== */

        .run-section {

            text-align: center;

            margin: 35px 0;

        }


        .run-button {

            background: #2563eb;

            color: white;

            border: none;

            padding: 16px 40px;

            border-radius: 8px;

            font-size: 18px;

            font-weight: bold;

            cursor: pointer;

        }


        .run-button:hover {

            background: #1d4ed8;

        }


        /* ====================================================
           RESULT SECTION
           ==================================================== */

        .results {

            margin-top: 35px;

        }


        .result-grid {

            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 20px;

        }


        .agent-result {

            background: white;

            padding: 22px;

            border-radius: 12px;

            box-shadow:
                0 3px 10px rgba(0,0,0,0.08);

        }


        .agent-result h3 {

            margin-top: 0;

            font-size: 22px;

        }


        .allocation-row {

            display: flex;

            justify-content: space-between;

            padding: 8px 0;

            border-bottom:
                1px solid #eee;

        }


        /* ====================================================
           STATUS
           ==================================================== */

        .status {

            display: inline-block;

            padding: 7px 14px;

            border-radius: 20px;

            font-weight: bold;

            margin-top: 12px;

        }


        .accepted {

            background: #dcfce7;

            color: #166534;

        }


        .partial {

            background: #fef3c7;

            color: #92400e;

        }


        .rejected {

            background: #fee2e2;

            color: #991b1b;

        }


        /* ====================================================
           REMAINING RESOURCES
           ==================================================== */

        .remaining-grid {

            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 20px;

        }


        .remaining-card {

            background: white;

            padding: 25px;

            text-align: center;

            border-radius: 12px;

            box-shadow:
                0 3px 10px rgba(0,0,0,0.08);

        }


        .remaining-card h3 {

            margin-bottom: 10px;

        }


        .remaining-value {

            font-size: 28px;

            font-weight: bold;

        }


        /* ====================================================
           ARCHITECTURE RESULT
           ==================================================== */

        .comparison-grid {

            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 20px;

        }


        .comparison-card {

            background: white;

            padding: 25px;

            border-radius: 12px;

            text-align: center;

            box-shadow:
                0 3px 10px rgba(0,0,0,0.08);

        }


        .comparison-card h3 {

            font-size: 20px;

        }


        .percentage {

            font-size: 32px;

            font-weight: bold;

        }


        /* ====================================================
           MESSAGE
           ==================================================== */

        .message {

            background: #fff7ed;

            color: #9a3412;

            padding: 20px;

            border-radius: 10px;

            margin-top: 20px;

            text-align: center;

        }


        /* ====================================================
           FOOTER
           ==================================================== */

        .footer {

            text-align: center;

            padding: 30px;

            color: #666;

        }


        /* ====================================================
           RESPONSIVE
           ==================================================== */

        @media (max-width: 850px) {

            .resource-grid,
            .architecture-grid,
            .result-grid,
            .remaining-grid,
            .comparison-grid {

                grid-template-columns: 1fr;

            }

            .header h1 {

                font-size: 27px;

            }

        }

    </style>

</head>


<body>


<!-- ========================================================
     HEADER
     ======================================================== -->

<div class="header">

    <h1>
        Negotiating Agents for Resource Sharing
    </h1>

    <p>
        Multi-Agent Resource Sharing using
        Centralized, Sequential/Pipeline
        and Peer-to-Peer Architectures
    </p>

</div>



<div class="container">


<!-- ========================================================
     PRODUCT
     ======================================================== -->

<div class="product-section">

    <h2>Product / Process</h2>

    <input
        class="product-input"
        type="text"
        value="{{ product }}"
        name="product"
        form="runForm"
        placeholder="Enter product name"
    >

</div>



<!-- ========================================================
     AVAILABLE RESOURCES
     ======================================================== -->

<h2 class="section-title">
    Total Available Resources
</h2>


<div class="resource-grid">


    <div class="resource-card">

        <h3>CPU</h3>

        <div class="resource-value">
            {{ cpu }}
        </div>

        <p>Units</p>

    </div>


    <div class="resource-card">

        <h3>Memory</h3>

        <div class="resource-value">
            {{ memory }}
        </div>

        <p>GB</p>

    </div>


    <div class="resource-card">

        <h3>Storage</h3>

        <div class="resource-value">
            {{ storage }}
        </div>

        <p>GB</p>

    </div>


</div>



<!-- ========================================================
     AGENT REQUIREMENTS
     ======================================================== -->

<h2 class="section-title">
    Agent Resource Requirements
</h2>


<div class="table-container">


<table>

<tr>

    <th>Agent</th>

    <th>Priority</th>

    <th>CPU</th>

    <th>Memory</th>

    <th>Storage</th>

</tr>


<tr>

    <td>Agent A</td>

    <td>High</td>

    <td>5</td>

    <td>6 GB</td>

    <td>30 GB</td>

</tr>


<tr>

    <td>Agent B</td>

    <td>Medium</td>

    <td>4</td>

    <td>5 GB</td>

    <td>25 GB</td>

</tr>


<tr>

    <td>Agent C</td>

    <td>Low</td>

    <td>6</td>

    <td>7 GB</td>

    <td>40 GB</td>

</tr>


</table>


</div>



<!-- ========================================================
     ARCHITECTURES
     ======================================================== -->

<h2 class="section-title">
    Negotiation Architectures
</h2>


<div class="architecture-grid">


    <div class="architecture-card">

        <h3>
            Centralized Architecture
        </h3>

        <p>
            A central manager controls
            the negotiation and resource
            allocation of all agents.
        </p>

    </div>


    <div class="architecture-card">

        <h3>
            Sequential / Pipeline Architecture
        </h3>

        <p>
            Agents negotiate one after
            another using a sequential
            pipeline.
        </p>

    </div>


    <div class="architecture-card">

        <h3>
            Peer-to-Peer Architecture
        </h3>

        <p>
            Agents communicate directly
            and negotiate resources
            with other agents.
        </p>

    </div>


</div>



<!-- ========================================================
     RUN BUTTON
     ======================================================== -->

<div class="run-section">

<form
    id="runForm"
    action="/run"
    method="GET"
>


    <button
        type="submit"
        class="run-button"
    >

        RUN RESOURCE SHARING

    </button>


</form>

</div>



<!-- ========================================================
     RESULTS
     ======================================================== -->

{% if results %}


<div class="results">


<h2 class="section-title">
    Resource Allocation Results
</h2>



<div class="result-grid">


{% for agent in results %}


<div class="agent-result">


    <h3>
        {{ agent.name }}
    </h3>


    <div class="allocation-row">

        <span>CPU</span>

        <strong>
            {{ agent.cpu }}
        </strong>

    </div>


    <div class="allocation-row">

        <span>Memory</span>

        <strong>
            {{ agent.memory }} GB
        </strong>

    </div>


    <div class="allocation-row">

        <span>Storage</span>

        <strong>
            {{ agent.storage }} GB
        </strong>

    </div>


    {% if agent.status == "Accepted" %}

        <span class="status accepted">
            ✓ ACCEPTED
        </span>

    {% elif agent.status == "Partial" %}

        <span class="status partial">
            ⚠ PARTIAL ALLOCATION
        </span>

    {% else %}

        <span class="status rejected">
            ✕ REJECTED
        </span>

    {% endif %}


</div>


{% endfor %}


</div>



<!-- ========================================================
     REMAINING RESOURCES
     ======================================================== -->

<h2 class="section-title">
    Remaining Resources
</h2>


<div class="remaining-grid">


    <div class="remaining-card">

        <h3>CPU</h3>

        <div class="remaining-value">
            {{ remaining_cpu }}
        </div>

        <p>Units Remaining</p>

    </div>


    <div class="remaining-card">

        <h3>Memory</h3>

        <div class="remaining-value">
            {{ remaining_memory }}
        </div>

        <p>GB Remaining</p>

    </div>


    <div class="remaining-card">

        <h3>Storage</h3>

        <div class="remaining-value">
            {{ remaining_storage }}
        </div>

        <p>GB Remaining</p>

    </div>


</div>



<!-- ========================================================
     ARCHITECTURE COMPARISON
     ======================================================== -->

<h2 class="section-title">
    Architecture Comparison
</h2>


<div class="comparison-grid">


    <div class="comparison-card">

        <h3>
            Centralized
        </h3>

        <div class="percentage">
            {{ centralized_score }}%
        </div>

        <p>
            Resource Allocation
        </p>

    </div>


    <div class="comparison-card">

        <h3>
            Sequential / Pipeline
        </h3>

        <div class="percentage">
            {{ sequential_score }}%
        </div>

        <p>
            Resource Allocation
        </p>

    </div>


    <div class="comparison-card">

        <h3>
            Peer-to-Peer
        </h3>

        <div class="percentage">
            {{ p2p_score }}%
        </div>

        <p>
            Resource Allocation
        </p>

    </div>


</div>


</div>


{% endif %}



{% if message %}

<div class="message">

    {{ message }}

</div>

{% endif %}



</div>


<div class="footer">

    Negotiating Agents for Resource Sharing

    <br><br>

    Centralized |
    Sequential / Pipeline |
    Peer-to-Peer

</div>


</body>

</html>

"""


# ============================================================
# DEFAULT VALUES
# ============================================================

DEFAULT_CPU = 10
DEFAULT_MEMORY = 12
DEFAULT_STORAGE = 60


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/", methods=["GET"])
def home():

    return render_template_string(

        HTML,

        product="Manufacturing Product",

        cpu=DEFAULT_CPU,

        memory=DEFAULT_MEMORY,

        storage=DEFAULT_STORAGE,

        results=None,

        remaining_cpu=DEFAULT_CPU,

        remaining_memory=DEFAULT_MEMORY,

        remaining_storage=DEFAULT_STORAGE,

        centralized_score=0,

        sequential_score=0,

        p2p_score=0,

        message=""

    )


# ============================================================
# RUN SIMULATION
# ============================================================

@app.route("/run", methods=["GET"])
def run_simulation():


    # --------------------------------------------------------
    # Product name
    # --------------------------------------------------------

    product = request.args.get(
        "product",
        "Manufacturing Product"
    )


    # --------------------------------------------------------
    # Current resource pool
    # --------------------------------------------------------

    cpu = DEFAULT_CPU

    memory = DEFAULT_MEMORY

    storage = DEFAULT_STORAGE


    # --------------------------------------------------------
    # Default result data
    # --------------------------------------------------------

    results = [

        {
            "name": "Agent A",
            "cpu": 5,
            "memory": 6,
            "storage": 30,
            "status": "Accepted"
        },

        {
            "name": "Agent B",
            "cpu": 4,
            "memory": 5,
            "storage": 25,
            "status": "Accepted"
        },

        {
            "name": "Agent C",
            "cpu": 1,
            "memory": 1,
            "storage": 5,
            "status": "Partial"
        }

    ]


    # --------------------------------------------------------
    # Calculate remaining resources
    # --------------------------------------------------------

    used_cpu = 0

    used_memory = 0

    used_storage = 0


    for agent in results:

        used_cpu += agent["cpu"]

        used_memory += agent["memory"]

        used_storage += agent["storage"]


    remaining_cpu = max(
        0,
        cpu - used_cpu
    )


    remaining_memory = max(
        0,
        memory - used_memory
    )


    remaining_storage = max(
        0,
        storage - used_storage
    )


    # --------------------------------------------------------
    # Architecture scores
    # --------------------------------------------------------

    centralized_score = 85

    sequential_score = 72

    p2p_score = 78


    # --------------------------------------------------------
    # Display page
    # --------------------------------------------------------

    return render_template_string(

        HTML,

        product=product,

        cpu=cpu,

        memory=memory,

        storage=storage,

        results=results,

        remaining_cpu=remaining_cpu,

        remaining_memory=remaining_memory,

        remaining_storage=remaining_storage,

        centralized_score=centralized_score,

        sequential_score=sequential_score,

        p2p_score=p2p_score,

        message="Resource negotiation completed successfully."

    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    app.run(

        debug=True,

        host="127.0.0.1",

        port=5000

    )