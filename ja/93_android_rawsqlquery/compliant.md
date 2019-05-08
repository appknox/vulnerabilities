
以下は、Prepeared SQL文の使用例です。

    PreparedStatement pstmt = con.prepareStatement("UPDATE EMPLOYEES SET SALARY = ? WHERE ID = ?");
    pstmt.setBigDecimal(1, 153833.00)
    pstmt.setInt(2, 110592)

