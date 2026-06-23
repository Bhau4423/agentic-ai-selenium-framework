package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TablesPage;

public class VerifyActionControlsAbsenceTest extends BaseTest {

    @Test
    public void verifyActionControlsAbsence() {

        TablesPage page = new TablesPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}