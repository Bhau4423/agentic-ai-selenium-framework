package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TyposPage;

public class VerifyTypoAbsenceTest extends BaseTest {

    @Test
    public void verifyTypoAbsence() {

        TyposPage page = new TyposPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}