package simulation.generator;

import java.io.File;
import java.io.FileOutputStream;

import simulation.generator.app.Application;
import simulation.generator.app.CyberShake;
import simulation.generator.app.Genome;
import simulation.generator.app.Montage;
import simulation.generator.app.LIGO;
import simulation.generator.app.SIPHT;

/**
 * Generate several workflows for each application.
 * 
 * @author Gideon Juve <juve@usc.edu>
 */
public class RunAll {
	public static void run(Application app, File outfile, String... args) throws Exception {
		app.generateWorkflow(args);
		app.printWorkflow(new FileOutputStream(outfile));
	}

	public static void main(String[] args) throws Exception {

		run(new CyberShake(), new File("CyberShake_30.xml"), "-n", "30");
		run(new CyberShake(), new File("CyberShake_50.xml"), "-n", "50");
		run(new CyberShake(), new File("CyberShake_100.xml"), "-n", "100");
		run(new CyberShake(), new File("CyberShake_200.xml"), "-n", "200");
		run(new CyberShake(), new File("CyberShake_300.xml"), "-n", "300");
		run(new CyberShake(), new File("CyberShake_400.xml"), "-n", "400");
		run(new CyberShake(), new File("CyberShake_500.xml"), "-n", "500");
		run(new CyberShake(), new File("CyberShake_700.xml"), "-n", "700");
		run(new CyberShake(), new File("CyberShake_1000.xml"), "-n", "1000");

		run(new Montage(), new File("Montage_25.xml"), "-n", "25");
		run(new Montage(), new File("Montage_50.xml"), "-n", "50");
		run(new Montage(), new File("Montage_100.xml"), "-n", "100");
		run(new Montage(), new File("Montage_200.xml"), "-n", "200");
		run(new Montage(), new File("Montage_300.xml"), "-n", "300");
		run(new Montage(), new File("Montage_400.xml"), "-n", "400");
		run(new Montage(), new File("Montage_500.xml"), "-n", "500");
		run(new Montage(), new File("Montage_700.xml"), "-n", "700");
		run(new Montage(), new File("Montage_1000.xml"), "-n", "1000");

		run(new LIGO(), new File("Ligo_100.xml"), "-n", "100");
		run(new LIGO(), new File("Ligo_200.xml"), "-n", "200");
		run(new LIGO(), new File("Ligo_300.xml"), "-n", "300");
		run(new LIGO(), new File("Ligo_400.xml"), "-n", "400");
		run(new LIGO(), new File("Ligo_500.xml"), "-n", "500");
		run(new LIGO(), new File("Ligo_700.xml"), "-n", "700");
		run(new LIGO(), new File("Ligo_1000.xml"), "-n", "1000");

		run(new Genome(), new File("Epigenomics_24.xml"), "-n", "24");
		run(new Genome(), new File("Epigenomics_46.xml"), "-n", "46");		
		run(new Genome(), new File("Epigenomics_100.xml"), "-n", "100");
		run(new Genome(), new File("Epigenomics_200.xml"), "-n", "200");
		run(new Genome(), new File("Epigenomics_300.xml"), "-n", "300");
		run(new Genome(), new File("Epigenomics_400.xml"), "-n", "400");
		run(new Genome(), new File("Epigenomics_500.xml"), "-n", "500");
		run(new Genome(), new File("Epigenomics_700.xml"), "-n", "700");
		run(new Genome(), new File("Epigenomics_1000.xml"), "-n", "1000");
		run(new Genome(), new File("Epigenomics_997.xml"), "-n", "997");

		run(new LIGO(), new File("Inspiral_30.xml"), "-n", "30");
		run(new LIGO(), new File("Inspiral_50.xml"), "-n", "50");
		run(new LIGO(), new File("Inspiral_100.xml"), "-n", "100");
		run(new LIGO(), new File("Inspiral_200.xml"), "-n", "200");
		run(new LIGO(), new File("Inspiral_300.xml"), "-n", "300");
		run(new LIGO(), new File("Inspiral_400.xml"), "-n", "400");
		run(new LIGO(), new File("Inspiral_500.xml"), "-n", "500");
		run(new LIGO(), new File("Inspiral_700.xml"), "-n", "700");
		run(new LIGO(), new File("Inspiral_1000.xml"), "-n", "1000");

		run(new SIPHT(), new File("Sipht_30.xml"), "-n", "30");
		run(new SIPHT(), new File("Sipht_60.xml"), "-n", "60");
		run(new SIPHT(), new File("Sipht_100.xml"), "-n", "100");
		run(new SIPHT(), new File("Sipht_200.xml"), "-n", "200");
		run(new SIPHT(), new File("Sipht_300.xml"), "-n", "300");
		run(new SIPHT(), new File("Sipht_400.xml"), "-n", "400");
		run(new SIPHT(), new File("Sipht_500.xml"), "-n", "500");
		run(new SIPHT(), new File("Sipht_700.xml"), "-n", "700");
		run(new SIPHT(), new File("Sipht_1000.xml"), "-n", "1000");

	}
}
