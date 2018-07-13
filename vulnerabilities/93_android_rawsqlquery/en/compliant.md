
Below is an example of how to use Prepeared SQL statement:

    PreparedStatement pstmt = con.prepareStatement("UPDATE EMPLOYEES SET SALARY = ? WHERE ID = ?");
    pstmt.setBigDecimal(1, 153833.00)
    pstmt.setInt(2, 110592)

